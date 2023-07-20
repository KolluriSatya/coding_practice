BINARIES="evergreen"
make CFLAGS="-w -O3 -I$PREFIX/include -L$PREFIX/lib"

mkdir -p ${PREFIX}/bin
cp $BINARIES $PREFIX/bin
mkdir -p $PREFIX/doc/evergreen/scripts

# copy script to download database
chmod +x ${RECIPE_DIR}/download-evergreen-db.sh
cp ${RECIPE_DIR}/download-evergreen-db.sh ${PREFIX}/bin/download-evergreen-db.sh
