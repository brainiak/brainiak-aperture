### Setting Things Up

Before you can run this notebook, you will have to take the following steps to set up our framework:

**1.** Clone the [brainiak aperture repo](https://github.com/brainiak/brainiak-aperture.git) and the [rtcloud framework repo](https://github.com/brainiak/rt-cloud.git). The location of the repositories do not matter but you should make a note of the paths.

**2.** Follow [Step 1](https://github.com/brainiak/rt-cloud#step-1-install-mini-conda-and-nodejs) of the installation instructions for the rtcloud framework: check to see if you have conda, Node.js, and NPM installed. Install these packages if necessary.

**3.** Create a conda environment that will be specific for the rtcloud framework and activate it:

- `cd /PATH_TO_RTCLOUD/rt-cloud`
- `conda env create -f environment.yml`
- `conda activate rtcloud`

**4.** Install and build node module dependencies.

- `cd /PATH_TO_RTCLOUD/rt-cloud/web`
- `npm install`
- `npm run build`

**5.** On the terminal, create a global variable to the full path for the rtcloud framework repo.

- `export RTCLOUD_PATH=/Users/PATH_TO_THE_REPO/rt-cloud/`
- Confirm you did this correctly by running `ECHO $RTCLOUD_PATH`, which should return the correct path.
    
**6.** You're all set! Enjoy going through this tutorial.

#### Common Mistakes or Issues

- If you get a blank blue screen when you open the localhost with the web server, then you forgot to follow Step 4 above.
- The `/tmp/notebook-simdata` folder is in your root directory. To get there, do `cd ~`. You want to delete this `notebook-simdata` folder whenever you want to similate the synthetic data being produced in real-time.
- If `rtCommon` can't be found, then you forgot to run Step 5 above.