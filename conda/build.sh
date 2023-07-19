#!/bin/bash

mkdir -p ${PREFIX}/bin

conda env create --file evergreen/scripts/environment.yml

# copy script to download database
chmod +x ${RECIPE_DIR}/download-evergreen-db.sh
cp ${RECIPE_DIR}/download-evergreen-db.sh ${PREFIX}/bin/download-evergreen-db.sh
