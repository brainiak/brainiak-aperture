FROM contextlab/cdl-jupyter:3.7

LABEL maintainer="Paxton Fitzpatrick <paxton.c.fitzpatrick@dartmouth.edu>"

ARG PORT=8888

ENV NOTEBOOK_PORT $PORT

RUN apt-get update --fix-missing \
    && eatmydata apt-get install -y --no-install-recommends \
        g++ \
        git \
        unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && conda install -Sy \
        bokeh=2.2.2 \
        ffmpeg=4.3.1 \
        holoviews=1.13.4 \
        mpi4py=3.0.3 \
        nibabel=3.1.1 \
        nilearn=0.6.2 \
    && conda clean -afy \
    && pip install \
        timecorr==0.1.5 \
        nltools==0.4.2 \
        git+https://github.com/ContextLab/hypertools.git@3f45375682a8f12a1278dd1720290d75a50062a9 \
        git+https://github.com/brainiak/brainiak.git@938151acff10cf49954f2c9933278de327b9da9d \
    && rm -rf ~/.cache/pip \
    && mkdir /data \
    && wget -qO /data/pieman.zip https://drive.google.com/open?id=1IBA39ZZjeGS1u_DvZdiw1AZZQMS3K5q0 \
    && unzip /data/pieman.zip \
    && rm /data/pieman.zip
