BINARIES="parallel_snp_pipeline"
make CFLAGS=="-w -O3 -I$PREFIX/include -L$PREFIX/lib"
mkdir -p ${PREFIX}/bin
cp $BINARIES $PREFIX/bin

