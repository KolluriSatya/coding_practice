#!/bin/bash

# Activate the virtual environment
source ${PREFIX}/bin/activate
mkdir -p ${PREFIX}/bin
chmod +x ~/coding_practice/parallel_snp_pipeline.py
cp parallel_snp_pipeline.py ${PREFIX}/bin/parallel_snp_pipeline.py
