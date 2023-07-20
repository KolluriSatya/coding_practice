#!/bin/bash

HR_DATABASE=${PREFIX}/share/${PKG_NAME}-${PKG_VERSION}/database
sed -i ="s=BIOCONDA_SED_REPLACE=$HR_DATABASE=" parallel_snp_pipeline.py

#copy evergreen
mkdir -p ${PREFIX}/bin
chmod +x parallel_snp_pipeline.py
cp parallel_snp_pipeline.py ${PREFIX}/bin/parallel_snp_pipeline.py

# copy script to download database
chmod +x ${RECIPE_DIR}/download-evergreen-db.sh
cp ${RECIPE_DIR}/download-evergreen-db.sh ${PREFIX}/bin/download-evergreen-db.sh

# Build database
mkdir -p ${HR_DATABASE}
bash -x ${PREFIX}/bin/download-db.sh ${HR_DATABASE}

# set PLASMID_DB variable on env activation
mkdir -p ${PREFIX}/etc/conda/activate.d ${PREFIX}/etc/conda/deactivate.d
cat <<EOF >> ${PREFIX}/etc/conda/activate.d/parallel_snp_pipeline.sh
export EVERGREEN_DB =${HR_DATABASE}
EOF

cat <<EOF >> ${PREFIX}/etc/conda/deactivate.d/parallel_snp_pipeline.sh
unset EVERGREEN_DB
EOF