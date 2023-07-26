#!/usr/bin/env bash

conda pack --prefix /opt/conda/conda-bld/flankophile_1690397023826/_build_env --output "$BUILD_DIR/flankophile.git"
mkdir -p ${PREFIX}/bin
cd /bin/abricate
chmod 777 /bin//gff_to_gggenes.py
sudo cp /bin//gff_to_gggenes.py  ${PREFIX}/bin/gff_to_gggenes.py
