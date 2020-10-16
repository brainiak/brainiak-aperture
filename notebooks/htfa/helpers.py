import numpy as np
import pandas as pd
import nibabel as nib
from nilearn.input_data import NiftiMasker
import nilearn.plotting as niplot
import matplotlib as mpl
import holoviews as hv
import timecorr as tc
import os
import warnings

hv.extension('bokeh')
hv.output(size=200)

def nii2cmu(nifti_file, mask_file=None):
    '''
    inputs:
      nifti_file: a filename of a .nii or .nii.gz file to be converted into
                  CMU format
                  
      mask_file: a filename of a .nii or .nii.gz file to be used as a mask; all
                 zero-valued voxels in the mask will be ignored in the CMU-
                 formatted output.  If ignored or set to None, no voxels will
                 be masked out.
    
    outputs:
      Y: a number-of-timepoints by number-of-voxels numpy array containing the
         image data.  Each row of Y is an fMRI volume in the original nifti
         file.
      
      R: a number-of-voxels by 3 numpy array containing the voxel locations.
         Row indices of R match the column indices in Y.
    '''
    def fullfact(dims):
        '''
        Replicates MATLAB's fullfact function (behaves the same way)
        '''
        vals = np.asmatrix(range(1, dims[0] + 1)).T
        if len(dims) == 1:
            return vals
        else:
            aftervals = np.asmatrix(fullfact(dims[1:]))
            inds = np.asmatrix(np.zeros((np.prod(dims), len(dims))))
            row = 0
            for i in range(aftervals.shape[0]):
                inds[row:(row + len(vals)), 0] = vals
                inds[row:(row + len(vals)), 1:] = np.tile(aftervals[i, :], (len(vals), 1))
                row += len(vals)
            return inds
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        
        img = nib.load(nifti_file)
        mask = NiftiMasker(mask_strategy='background')
        if mask_file is None:
            mask.fit(nifti_file)
        else:
            mask.fit(mask_file)
    
    hdr = img.header
    S = img.get_sform()
    vox_size = hdr.get_zooms()
    im_size = img.shape
    
    if len(img.shape) > 3:
        N = img.shape[3]
    else:
        N = 1
    
    Y = np.float64(mask.transform(nifti_file)).copy()
    vmask = np.nonzero(np.array(np.reshape(mask.mask_img_.dataobj, (1, np.prod(mask.mask_img_.shape)), order='C')))[1]
    vox_coords = fullfact(img.shape[0:3])[vmask, ::-1]-1
    
    R = np.array(np.dot(vox_coords, S[0:3, 0:3])) + S[:3, 3]
    
    return {'Y': Y, 'R': R}

def cmu2nii(Y, R, template=None):
    '''
    inputs:
      Y: a number-of-timepoints by number-of-voxels numpy array containing the
         image data.  Each row of Y is an fMRI volume in the original nifti
         file.
      
      R: a number-of-voxels by 3 numpy array containing the voxel locations.
         Row indices of R match the column indices in Y.
      
      template: a filename of a .nii or .nii.gz file to be used as an image
                template.  Header information of the outputted nifti images will
                be read from the header file.  If this argument is ignored or
                set to None, header information will be inferred based on the
                R array.
    
    outputs:
      nifti_file: a filename of a .nii or .nii.gz file to be converted into
                  CMU format
                  
      mask_file: a filename for a .nii or .nii.gz file to be used as a mask; all
                 zero-valued voxels in the mask will be ignored in the CMU-
                 formatted output
    
    outputs:
      img: a nibabel Nifti1Image object containing the fMRI data
    '''
    Y = np.array(Y, ndmin=2)
    img = nib.load(template)
    S = img.affine
    locs = np.array(np.dot(R - S[:3, 3], np.linalg.inv(S[0:3, 0:3])), dtype='int')
    
    data = np.zeros(tuple(list(img.shape)[0:3]+[Y.shape[0]]))
    
    # loop over data and locations to fill in activations
    for i in range(Y.shape[0]):
        for j in range(R.shape[0]):
            data[locs[j, 0], locs[j, 1], locs[j, 2], i] = Y[i, j]
    
    return nib.Nifti1Image(data, affine=img.affine)

def animate_connectome(nodes, connectomes, figdir='frames', force_refresh=False):
    '''
    inputs:
      nodes: a K by 3 array of node center locations
      
      connectomes: a T by ((K^2 - K)/2) array of per-timepoint connectomes.
                   Each timepoint's connectime is represented in a vectorized
                   (squareform) format.
      
      figdir: where to save temporary files and final output
      
      force_refresh: if True, overwrite existing temporary files.  If False,
                     re-use existing temporary files and generate only the
                     temporary files that do not yet exist.
    
    outputs:
      ani: a matplotlib FuncAnimation object
    '''
    
    if not os.path.exists(figdir):
        os.makedirs(figdir)
    
    #save a jpg file for each frame (this takes a while, so don't re-do already made images)
    def get_frame(t, fname):
        if force_refresh or not os.path.exists(fname):
            niplot.plot_connectome(sd.squareform(connectomes[t, :]),
                                   nodes,
                                   node_color='k',
                                   edge_threshold='75%',
                                   output_file=fname)
    
    timepoints = np.arange(connectomes.shape[0])
    fnames = [os.path.join(figdir, str(t) + '.jpg') for t in timepoints]
    tmp = [get_frame(t, f) for zip(timepoints, fnames)]
    
    #create a movie frame from each of the images we just made
    mpl.pyplot.close()
    fig = mpl.pyplot.figure()
    
    def get_im(fname):
        #print(fname)
        mpl.pyplot.axis('off')
        return mpl.pyplot.imshow(mpl.pyplot.imread(fname), animated=True)
    
    ani = mpl.animation.FuncAnimation(fig, get_im, fnames, interval=50)    
    return ani

def mat2chord(connectome, cthresh=0.25):
    '''
    inputs:
      connectome: K by K connectivity matrix
      
      cthresh: only show connections in the top (cthresh*100)%; default = 0.25
    
    outputs:
      chord: a holoviews.Chord object displaying the connectome as a chord
             diagram
    '''
    
    def mat2links(x, ids):
        links = []
        for i in range(x.shape[0]):
            for j in range(i):
                links.append({'source': ids[i], 'target': ids[j], 'value': np.abs(x[i, j]), 'sign': np.sign(x[i, j])})
        return pd.DataFrame(links)
    
    K = connectome.shape[0]
    nodes = pd.DataFrame({'ID': range(K), 'Name': [f'{i}' for i in range(K)]})
    
    links = mat2links(connectome, nodes['Name'])
    chord = hv.Chord((links, hv.Dataset(nodes, 'ID'))).select(value=(cthresh, None))
    chord.opts(
        opts.Chord(cmap='Category20', edge_cmap='Category20', edge_color=dim('source').str(), labels='Name', node_color=dim('ID').str())
    )
    return chord

def animate_chord(connectomes, cthresh=0.25):
    '''
    inputs:
      connectomes: a T by [((K^2 - K)/2) + K] array of per-timepoint connectomes.
                   Each timepoint's connectime is represented in a vectorized
                   format *including the diagonal* (i.e., self connections).
      
      cthresh: only show connections in the top (cthresh*100)%; default = 0.25
    
    outputs:
      hmap: a holoviews.HoloMap object containing an interactive animation
      
    '''
    hv.output(max_frames=x.shape[0])
    renderer = hv.renderer('bokeh')
    return hv.HoloMap({t: mat2chord(tc.vec2mat(x[t, :]), cthresh=cthresh) for t in range(x.shape[0])}, kdims='Time (TRs)')
