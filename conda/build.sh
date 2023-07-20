#!/bin/bash

mkdir -p ${PREFIX}/scripts

chmod +x parallel_snp_pipeline.py
cp parallel_snp_pipeline.py  ${PREFIX}/scripts/parallel_snp_pipeline.py

# copy script to download database
chmod +x ${RECIPE_DIR}/download-evergreen-db.sh
cp ${RECIPE_DIR}/download-evergreen-db.sh ${PREFIX}/scripts/download-evergreen-db.sh
