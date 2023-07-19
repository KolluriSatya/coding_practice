#!/usr/bin/env bash

echo "Downloading lastest version of the database to current directory..."

cd /path/to/analysis_dir
mkdir results_db
mkdir output
mkdir logs

mkdir cgmlstfinder_db
cd cgmlstfinder_db

wget https://cge.food.dtu.dk/services/Evergreen/etc/database.tar.gz
tar -xzf database.tar.gz

# KMA database with default homology reduction settings
mkdir hr_database
mkdir hr_database/current

# Start environment when running the scripts
conda activate evergreen

# run database builder with default settings
build_database_chr.py -r $PWD/scripts/refseq_bacterial_complete_chromosomes_2021.lst -o $PWD/hr_database/current
