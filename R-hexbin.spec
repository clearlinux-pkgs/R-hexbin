#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-hexbin
Version  : 1.28.2
Release  : 35
URL      : https://cran.r-project.org/src/contrib/hexbin_1.28.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/hexbin_1.28.2.tar.gz
Summary  : Hexagonal Binning Routines
Group    : Development/Tools
License  : GPL-2.0
Requires: R-hexbin-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-hexbin package.
Group: Libraries

%description lib
lib components for the R-hexbin package.


%prep
%setup -q -c -n hexbin
cd %{_builddir}/hexbin

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610121536

%install
export SOURCE_DATE_EPOCH=1610121536
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hexbin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hexbin
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hexbin
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc hexbin || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/hexbin/DESCRIPTION
/usr/lib64/R/library/hexbin/INDEX
/usr/lib64/R/library/hexbin/Meta/Rd.rds
/usr/lib64/R/library/hexbin/Meta/data.rds
/usr/lib64/R/library/hexbin/Meta/features.rds
/usr/lib64/R/library/hexbin/Meta/hsearch.rds
/usr/lib64/R/library/hexbin/Meta/links.rds
/usr/lib64/R/library/hexbin/Meta/nsInfo.rds
/usr/lib64/R/library/hexbin/Meta/package.rds
/usr/lib64/R/library/hexbin/Meta/vignette.rds
/usr/lib64/R/library/hexbin/NAMESPACE
/usr/lib64/R/library/hexbin/R/hexbin
/usr/lib64/R/library/hexbin/R/hexbin.rdb
/usr/lib64/R/library/hexbin/R/hexbin.rdx
/usr/lib64/R/library/hexbin/data/NHANES.rda
/usr/lib64/R/library/hexbin/doc/hexagon_binning.R
/usr/lib64/R/library/hexbin/doc/hexagon_binning.Rnw
/usr/lib64/R/library/hexbin/doc/hexagon_binning.pdf
/usr/lib64/R/library/hexbin/doc/index.html
/usr/lib64/R/library/hexbin/help/AnIndex
/usr/lib64/R/library/hexbin/help/aliases.rds
/usr/lib64/R/library/hexbin/help/hexbin.rdb
/usr/lib64/R/library/hexbin/help/hexbin.rdx
/usr/lib64/R/library/hexbin/help/paths.rds
/usr/lib64/R/library/hexbin/html/00Index.html
/usr/lib64/R/library/hexbin/html/R.css
/usr/lib64/R/library/hexbin/tests/hdiffplot.R
/usr/lib64/R/library/hexbin/tests/hdiffplot.Rout.save
/usr/lib64/R/library/hexbin/tests/hray.R
/usr/lib64/R/library/hexbin/tests/hray.Rout.save
/usr/lib64/R/library/hexbin/tests/large.R
/usr/lib64/R/library/hexbin/tests/large.Rout.save
/usr/lib64/R/library/hexbin/tests/viewp-ex.R
/usr/lib64/R/library/hexbin/tests/viewp-ex.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/hexbin/libs/hexbin.so
/usr/lib64/R/library/hexbin/libs/hexbin.so.avx2
/usr/lib64/R/library/hexbin/libs/hexbin.so.avx512
