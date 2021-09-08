#!/bin/bash
wget -nc https://dataspace.princeton.edu/bitstream/88435/dsp01dn39x4181/2/Corr_MVPA_archive.tar.gz
test ! -e Corr_MVPA_Data_dataspace && tar xzkvf Corr_MVPA_archive.tar.gz Corr_MVPA_Data_dataspace/Participant_01_rest_run01.nii

