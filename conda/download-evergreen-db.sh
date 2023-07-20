#!/usr/bin/env bash

echo "Downloading lastest version of the database to current directory..."

cd /path/to/analysis_dir
mkdir results_db
mkdir output
mkdir logs

wget https://cge.food.dtu.dk/services/Evergreen/etc/database.tar.gz
tar -xzf database.tar.gz --strip-components 1

echo "Installing the spatyper database with KMA"
python INSTALL.py

echo "The evergreen database has been downloaded and installed."

exit 0
