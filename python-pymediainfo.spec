# Created by pyp2rpm-3.3.1
%global pypi_name pymediainfo

Name:           python-%{pypi_name}
Version:        6.1.0
Release:        1
Summary:        A Python wrapper for the mediainfo library
Group:          Development/Python
License:        MIT
URL:            https://github.com/sbraz/pymediainfo
Source0:        https://pypi.io/packages/source/p/pymediainfo/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

# Required for tests
#BuildRequires:  mediainfo
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  locales-en
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(funcsigs)
BuildRequires:  python3dist(pluggy)
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(simplejson)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(tomli)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
This small package is a wrapper around the MediaInfo library.

%package -n python-%{pypi_name}-doc
Summary:        pymediainfo documentation

%description -n python-%{pypi_name}-doc
Documentation for pymediainfo

%prep
# Make sure the tarball (containing non-ASCII filenames)
# can be extracted correctly
export LC_ALL=en_US.utf-8
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%files
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info

%files -n python-%{pypi_name}-doc
%doc html
