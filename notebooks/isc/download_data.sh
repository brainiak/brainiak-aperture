#!/bin/bash

# Test to see if the extracted data is present, if not, download the archive. The python notebook handles extraction and
# deleting of the archive for us.
test ! -e brainiak-aperture-isc-data && wget -nc https://zenodo.org/record/4300904/files/brainiak-aperture-isc-data.tgz
