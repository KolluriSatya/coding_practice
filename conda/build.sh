BINARIES= "parallel_snp_pipeline"
make CFLAGS="-w -03 -PREFIX/include -L$PREFIX/lib"
mkdir -p ${PREFIX}/bin
cp $BINARIES ${PREFIX}/bin
mkdir -p $PREFIX/doc/evergreen

