#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lambda.r
Version  : 1.2.4
Release  : 44
URL      : https://cran.r-project.org/src/contrib/lambda.r_1.2.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lambda.r_1.2.4.tar.gz
Summary  : Modeling Data with Functional Programming
Group    : Development/Tools
License  : LGPL-3.0
Requires: R-formatR
BuildRequires : R-formatR
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n lambda.r
cd %{_builddir}/lambda.r

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589826996

%install
export SOURCE_DATE_EPOCH=1589826996
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lambda.r
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lambda.r
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lambda.r
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lambda.r || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lambda.r/DESCRIPTION
/usr/lib64/R/library/lambda.r/INDEX
/usr/lib64/R/library/lambda.r/Meta/Rd.rds
/usr/lib64/R/library/lambda.r/Meta/features.rds
/usr/lib64/R/library/lambda.r/Meta/hsearch.rds
/usr/lib64/R/library/lambda.r/Meta/links.rds
/usr/lib64/R/library/lambda.r/Meta/nsInfo.rds
/usr/lib64/R/library/lambda.r/Meta/package.rds
/usr/lib64/R/library/lambda.r/NAMESPACE
/usr/lib64/R/library/lambda.r/R/lambda.r
/usr/lib64/R/library/lambda.r/R/lambda.r.rdb
/usr/lib64/R/library/lambda.r/R/lambda.r.rdx
/usr/lib64/R/library/lambda.r/help/AnIndex
/usr/lib64/R/library/lambda.r/help/aliases.rds
/usr/lib64/R/library/lambda.r/help/lambda.r.rdb
/usr/lib64/R/library/lambda.r/help/lambda.r.rdx
/usr/lib64/R/library/lambda.r/help/paths.rds
/usr/lib64/R/library/lambda.r/html/00Index.html
/usr/lib64/R/library/lambda.r/html/R.css
/usr/lib64/R/library/lambda.r/tests/test-all.R
/usr/lib64/R/library/lambda.r/tests/testit/test-auto_replace.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-auto_replace.2.R
/usr/lib64/R/library/lambda.r/tests/testit/test-auto_replace.3.R
/usr/lib64/R/library/lambda.r/tests/testit/test-dispatching.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-ellipsis_arguments.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-ellipsis_arguments.2.R
/usr/lib64/R/library/lambda.r/tests/testit/test-examples.R
/usr/lib64/R/library/lambda.r/tests/testit/test-factorial.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-factorial.2.R
/usr/lib64/R/library/lambda.r/tests/testit/test-fill_args.R
/usr/lib64/R/library/lambda.r/tests/testit/test-function_args.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-function_type.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-heaviside_step.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-heaviside_step.2.R
/usr/lib64/R/library/lambda.r/tests/testit/test-infix.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-optional_arguments.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-optional_arguments.2.R
/usr/lib64/R/library/lambda.r/tests/testit/test-parse_transforms.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-parse_transforms.2.R
/usr/lib64/R/library/lambda.r/tests/testit/test-parse_transforms.3.R
/usr/lib64/R/library/lambda.r/tests/testit/test-pattern_matching.R
/usr/lib64/R/library/lambda.r/tests/testit/test-taylor_series.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-type_any_type.R
/usr/lib64/R/library/lambda.r/tests/testit/test-type_ellipsis.R
/usr/lib64/R/library/lambda.r/tests/testit/test-type_functions.R
/usr/lib64/R/library/lambda.r/tests/testit/test-type_inheritance.R
/usr/lib64/R/library/lambda.r/tests/testit/test-type_integer_inheritance.R
/usr/lib64/R/library/lambda.r/tests/testit/test-type_variable.1.R
/usr/lib64/R/library/lambda.r/tests/testit/test-types.1.R
