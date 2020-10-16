## Installation
NOTE: The installation instructions to run this tutorial closely follow the instructions found on the [github repo for our real-time fMRI cloud framework](https://github.com/brainiak/rt-cloud). Please visit our repo for more information.

1. Pull the source code <code>git clone https://github.com/brainiak/brainiak-aperture/blob/rtcloud/notebooks/real-time/rtcloud_environment.yml</code> **NOTE: Change this link after this branch has been merged with the master!!**

2. Navigate to this specific tutorial: <code>cd brainiak-aperture/notebooks/real-time/</code>

3. Create a conda environment for this specific tutorial: <code>conda env create -f rtcloud_environment.yml</code>
    - Check if you have mini-conda already installed. In a terminal run <code>conda -V</code>
        - *Mac Specific:* [Install Mini-Conda](https://docs.conda.io/en/latest/miniconda.html)
        - *Linux Specific:* Install Mini-Conda
            - <code>wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh</code>
            - <code>bash Miniconda3-latest-Linux-x86_64.sh -b</code>

