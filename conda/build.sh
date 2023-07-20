#!/bin/bash

mkdir -p ${PREFIX}/bin

chmod +x parallel_snp_pipeline.py
cp parallel_snp_pipeline.py ${PREFIX}/bin/parallel_snp_pipeline.py

# copy script to download database
chmod +x ${RECIPE_DIR}/download-evergreen-db.sh
cp ${RECIPE_DIR}/download-evergreen-db.sh ${PREFIX}/bin/download-evergreen-db.sh
