# Created by pyp2rpm-3.3.1
%global pypi_name pymediainfo

Name:           python-%{pypi_name}
Version:        4.2.1
Release:        %mkrel 1
Summary:        A Python wrapper for the mediainfo library
Group:          Development/Python
License:        MIT
URL:            https://github.com/sbraz/pymediainfo
Source0:        https://pypi.io/packages/source/p/pymediainfo/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

# Required for tests
BuildRequires:  mediainfo
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  locales-en

%description
This small package is a wrapper around the MediaInfo library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-hypothesis
BuildRequires:  python3dist(funcsigs)
BuildRequires:  python3dist(pluggy)
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(simplejson)
BuildRequires:  python3dist(setuptools-scm)

%description -n python3-%{pypi_name}
This small package is a wrapper around the MediaInfo library.

%package -n python-%{pypi_name}-doc
Summary:        pymediainfo documentation

%description -n python-%{pypi_name}-doc
Documentation for pymediainfo

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

#check
#PYTHONPATH=$PWD %{__python2} setup.py test
#pushd %{py3dir}
#PYTHONPATH=$PWD %{__python3} setup.py test
#popd

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
