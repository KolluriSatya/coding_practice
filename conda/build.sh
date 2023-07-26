  GNU nano 6.2                                                                                                build.sh
#!/bin/bash

mkdir -p ${PREFIX}/bin

chmod +x ~/coding_practice/bin/abricate/gff_to_gggenes.py
cp gff_to_gggenes.py ${PREFIX}/bin/gff_to_gggenes.py
