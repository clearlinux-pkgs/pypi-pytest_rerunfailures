#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest_rerunfailures
Version  : 10.2
Release  : 39
URL      : https://files.pythonhosted.org/packages/83/07/4b24f61f9700bd0d11cad641180898d48f602f156254a43376ee759fb904/pytest-rerunfailures-10.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/07/4b24f61f9700bd0d11cad641180898d48f602f156254a43376ee759fb904/pytest-rerunfailures-10.2.tar.gz
Summary  : pytest plugin to re-run tests to eliminate flaky failures
Group    : Development/Tools
License  : MPL-2.0
Requires: pypi-pytest_rerunfailures-license = %{version}-%{release}
Requires: pypi-pytest_rerunfailures-python = %{version}-%{release}
Requires: pypi-pytest_rerunfailures-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(pytest)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
pytest-rerunfailures
        ====================

%package license
Summary: license components for the pypi-pytest_rerunfailures package.
Group: Default

%description license
license components for the pypi-pytest_rerunfailures package.


%package python
Summary: python components for the pypi-pytest_rerunfailures package.
Group: Default
Requires: pypi-pytest_rerunfailures-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest_rerunfailures package.


%package python3
Summary: python3 components for the pypi-pytest_rerunfailures package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_rerunfailures)
Requires: pypi(pytest)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-pytest_rerunfailures package.


%prep
%setup -q -n pytest-rerunfailures-10.2
cd %{_builddir}/pytest-rerunfailures-10.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649699604
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_rerunfailures
cp %{_builddir}/pytest-rerunfailures-10.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_rerunfailures/7a5895d25709ec140bb6861ae0814cca5a834248
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytest_rerunfailures/7a5895d25709ec140bb6861ae0814cca5a834248

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
