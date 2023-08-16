#!/bin/bash

mkdir -p ${PREFIX}/bin

chmod +x /scripts/parallel_snp_pipeline.py
cp /scripts/parallel_snp_pipeline.py ${PREFIX}/bin/parallel_snp_pipeline.py

# set PLASMID_DB variable on env activation
mkdir -p ${PREFIX}/etc/conda/activate.d ${PREFIX}/etc/conda/deactivate.d
cat <<EOF >> ${PREFIX}/etc/conda/activate.d/evergreen
export evergreen=${evergreen}
EOF

cat <<EOF >> ${PREFIX}/etc/conda/deactivate.d/evergreen.sh
unset evergreen
EOF
