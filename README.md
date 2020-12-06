# Overview
This repository hosts the example notebooks that are included as a companion to the paper [Kumar et al. (2020) *BrainIAK: Brain Imaging and Analysis Kit*](https://osf.io/preprints/...).  Instructions for running each analysis (including links to the relevant datasets and setup instructions) are included as part of each notebook.

# Contents
The following notebooks are included in the repository (section numbers from the
paper are noted in parentheses):
1. [Intersubject Correlation](notebooks/isc/ISC.ipynb) (ISC; Section 2.1)
2. [Shared Response Model](notebooks/srm/SRM.ipynb) (SRM; Section 2.2)
3. [Full Correlation Matrix Analysis](notebooks/fcma/FCMA_demo.ipynb) (FCMA; Section 2.3)
4. [Bayesian Representational Similarity Analysis](notebooks/brsa/brsa_demo.ipynb) (BRSA; Section 2.4)
5. [Event Segmentation](notebooks/eventseg/Event_Segmentation.ipynb) (Section 2.5)
6. [Topographic Factor Analysis](notebooks/htfa/htfa.ipynb) (TFA; Section 2.6)
7. [Inverted Encoding Model](notebooks/iem/iem.ipynb) (IEM; Section 2.7)
8. [Simulating Realistic fMRI Data](notebooks/fmrisim/fmrisim_multivariate_example.ipynb) (fmrisim; Section 2.8)
9. [Matrix-Normal Models](notebooks/matnormal/Matrix-normal%20model%20prototyping.ipynb) (Section 2.9.2)
10. [Real-Time fMRI Analysis](notebook/real-time/rtcloud_notebook.ipynb) (Section 3)

# Installation

Step 1. You need to install BrainIAK and related software to run these example notebooks. To install the software and configure an environment to run Jupyter notebooks, we have provided a variety of installation options as part of the BrainIAK tutorials: https://brainiak.org/tutorials.

Step 2. Once you complete installation in Step 1, you are ready to download the example notebooks, in this repository, and the associated data needed to run them. 

## Example Notebooks
Clone this repository: `git clone https://github.com/brainiak/brainiak-aperture.git`

## Data
The notebooks include instructions for downloading and using data. All the data used is publicly available.

### Examples whose installation instructions are different from the rest.
1. The [TFA notebook](notebooks/htfa/htfa.ipynb) comes with it's own Docker container, that includes all data and software required to run the notebook. You can follow the installation instructions in the notebook to run it.

2. The [Real-Time fMRI Analysis](notebook/real-time/rtcloud_notebook.ipynb) requires installing a web server, the instructions for which  may be found [here](https://github.com/brainiak/brainiak-aperture/blob/master/notebooks/real-time/README_INSTRUCTIONS.md)


# License
Like BrainIAK itself, these example are open-sourced and can be freely used, modified, and shared. They are licensed under the Apache License, Version 2.0. 
