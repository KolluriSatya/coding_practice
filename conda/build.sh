#!/usr/bin/env bash

mkdir -p ${PREFIX}/bin
cd /bin/abricate
chmod 777 /bin//gff_to_gggenes.py
sudo cp /bin//gff_to_gggenes.py  ${PREFIX}/bin/gff_to_gggenes.py
