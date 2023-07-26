#!/usr/bin/env bash

mkdir -p ${PREFIX}/bin
cd /coding_practice/bin/abricate
chmod 777 /coding_practice/bin//gff_to_gggenes.py
sudo cp /coding_practice/bin//gff_to_gggenes.py  ${PREFIX}/bin/gff_to_gggenes.py
