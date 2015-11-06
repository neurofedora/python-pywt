%define modname	pywavelets
%define pkgname PyWavelets

Name: 		python-%{modname}
Version: 	0.2.0
Release: 	1%{?dist}
Summary: 	Python module for wavelet transforms
Source0: 	%{pkgname}-%{version}.tar.bz2
Patch0:		PyWavelets-0.2.0-cython-and-libm-fix.patch
License: 	MIT
Group:		Development/Python
Url: 		http://www.pybytes.com/pywavelets/
Requires:	python-numpy
BuildRequires:	python-cython
BuildRequires:	python-sphinx

%description
PyWavelets is a Python wavelet transform module that includes:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox (tm)

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
%py2_build
%make -C doc html

%install
%py2_install

%files -n python2-%{modname}
%doc *.txt demo/ doc/build/html

%changelog
* Fri Nov 06 2015 Adrian Alves <alvesadrian@fedoraproject.org> 0.2.0-1
- Initial build
