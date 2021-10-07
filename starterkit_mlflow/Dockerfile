FROM ubuntu:18.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/miniconda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 curl sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*  

RUN apt-get update
RUN apt-get install -y git 

ARG PYTHON_VERSION="3.7"
ARG USERNAME="vscode"
ARG PROJECT_DIR="/workspace/"
ARG MINICONDA_VERSION="4.7.12.1"
ARG JUPTER_LAB_VERSION="2.1.0"

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/miniconda && \
    rm ~/miniconda.sh && \
    /opt/miniconda/bin/conda clean -tipsy

RUN conda install -y conda python=${PYTHON_VERSION}

RUN conda install -c conda-forge  tini jupyterlab

RUN jupyter notebook --generate-config
