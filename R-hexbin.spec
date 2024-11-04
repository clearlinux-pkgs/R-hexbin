#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-hexbin
Version  : 1.28.4
Release  : 57
URL      : https://cran.r-project.org/src/contrib/hexbin_1.28.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/hexbin_1.28.4.tar.gz
Summary  : Hexagonal Binning Routines
Group    : Development/Tools
License  : GPL-2.0
Requires: R-hexbin-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-hexbin package.
Group: Libraries

%description lib
lib components for the R-hexbin package.


%prep
%setup -q -n hexbin
pushd ..
cp -a hexbin buildavx2
popd
pushd ..
cp -a hexbin buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725548383

%install
export SOURCE_DATE_EPOCH=1725548383
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/R/library/hexbin/libs/hexbin.so
/V4/usr/lib64/R/library/hexbin/libs/hexbin.so
/usr/lib64/R/library/hexbin/libs/hexbin.so
