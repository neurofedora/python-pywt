%define modname pywavelets
%define pkgname PyWavelets

Name:           python-%{modname}
Version:        0.2.2
Release:        1%{?dist}
Summary:        PyWavelets is a Python wavelet transforms module
License:        MIT
Group:          Development/Libraries/Python
Url:            http://pypi.python.org/pypi/PyWavelets/
Source0:        https://pypi.python.org/packages/source/P/%{pkgname}/%{pkgname}-%{version}.zip
BuildRequires:  unzip
BuildRequires:  python-Cython
BuildRequires:  python-devel
BuildRequires:  python-numpy-devel
BuildRequires:  python-Pygments
BuildRequires:  python-Sphinx

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
Summary:        This package contains the HMTL documentation of %{name}
Group:          Documentation/HTML

%description doc
PyWavelets is a Python wavelet transforms module that can do:

  * 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
  * 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
  * 1D and 2D Wavelet Packet decomposition and reconstruction
  * Computing Approximations of wavelet and scaling functions
  * Over seventy built-in wavelet filters and support for custom wavelets
  * Single and double precision calculations
  * Results compatibility with Matlab Wavelet Toolbox

This Package contains the documentation of %{name} in HTML format.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%py2_build

make -C doc PAPER=letter html

%install
%py2_install
# Remove hiden files
find doc/build/html -name '.*' -exec rm {} \;

# Fix python-bytecode-inconsistent-mtime
pushd %{buildroot}%{python_sitearch}
%py_compile .
popd


%files
%doc CHANGES.txt COPYING.txt README.rst THANKS.txt
%{python2_sitearch}/*

%files doc
%doc doc/build/html

%changelog
* Fri Nov 6 2015 Adrian Alves <alvesadrian@fedoraproject.org> 0.2.0-1
- Initial build
