#!/bin/bash

mkdir -p ${PREFIX}/bin

chmod +x ./bin/abricate/gff_to_gggenes.py
cp gff_to_gggenes.py ${PREFIX}/bin/gff_to_gggenes.py
