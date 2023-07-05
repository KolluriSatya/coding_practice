#!/bin/bash

# Update default DB location
PLASMIDFINDER_DB=${PREFIX}/share/${PKG_NAME}-${PKG_VERSION}/database
sed -i "s=BIOCONDA_SED_REPLACE=$PLASMIDFINDER_DB=" plasmidfinder.py

# Copy plasmidfinder
mkdir -p ${PREFIX}/bin
chmod +x plasmidfinder.py
cp plasmidfinder.py ${PREFIX}/bin/plasmidfinder.py

# copy script to download database
chmod +x ${RECIPE_DIR}/plasmidfinder-db.sh
cp ${RECIPE_DIR}/plasmidfinder-db.sh ${PREFIX}/bin/plasmidfinder-db.sh

# Build database
mkdir -p ${PLASMIDFINDER_DB}
bash -x ${PREFIX}/bin/plasmidfinder-db.sh ${PLASMIDFINDER_DB}

# set PLASMID_DB variable on env activation
mkdir -p ${PREFIX}/etc/conda/activate.d ${PREFIX}/etc/conda/deactivate.d
cat <<EOF >> ${PREFIX}/etc/conda/activate.d/plasmidfinder.sh
export PLASMID_DB=${PLASMIDFINDER_DB}
EOF

cat <<EOF >> ${PREFIX}/etc/conda/deactivate.d/plasmidfinder.sh
unset PLASMID_DB
EOF