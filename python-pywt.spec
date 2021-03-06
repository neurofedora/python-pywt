%define modname pywt
%define pkgname PyWavelets

Name:           python-%{modname}
Version:        0.3.0
Release:        2%{?dist}
Summary:        PyWavelets, wavelet transform module
License:        MIT
URL:            http://pywavelets.readthedocs.org/
Source0:        https://github.com/PyWavelets/pywt/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gcc

%description
PyWavelets is a Python wavelet transforms module that can do:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel Cython
BuildRequires:  numpy
BuildRequires:  python2-nose
BuildRequires:  python-sphinx
Requires:       numpy

%description -n python2-%{modname}
PyWavelets is a Python wavelet transforms module that can do:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-Cython
BuildRequires:  python3-numpy
BuildRequires:  python3-nose
BuildRequires:  python3-sphinx
Requires:       python3-numpy

%description -n python3-%{modname}
PyWavelets is a Python wavelet transforms module that can do:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

for lib in %{modname}/tests/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%py2_build
%py3_build

pushd doc
  export PYTHONPATH=`readlink -f ../build/lib.*-%{python3_version}`
  make html SPHINXBUILD=sphinx-build-%{python3_version}
  find -name '.buildinfo' -delete
popd

%install
%py2_install
%py3_install

%check
%{__python2} runtests.py --pythonpath %{buildroot}%{python2_sitearch} --verbose --no-build
%{__python3} runtests.py --pythonpath %{buildroot}%{python3_sitearch} --verbose --no-build

%files doc
%doc doc/build/html

%files -n python2-%{modname}
%license COPYING.txt
%doc README.rst THANKS.txt
%{python2_sitearch}/%{modname}/
%{python2_sitearch}/%{pkgname}*.egg-info

%files -n python3-%{modname}
%license COPYING.txt
%doc README.rst THANKS.txt
%{python3_sitearch}/%{modname}/
%{python3_sitearch}/%{pkgname}*.egg-info

%changelog
* Sat Nov 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-2
- One doc subpkg
- Drop shebangs from tests

* Fri Nov 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
