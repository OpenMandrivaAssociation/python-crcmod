%define oname crcmod

Name:     python-crcmod
Version:  1.7
Release:  8
Epoch:    0
Summary:  Creates functions that efficiently compute CRC's using table lookup
URL:      https://crcmod.sourceforge.net/
License:  MIT
Group:    Development/Python
Source0:  http://sourceforge.net/projects/crcmod/files/crcmod/crcmod-%{version}/crcmod-%{version}.tar.gz
Patch0:   crcmod-1.7-setuptools.patch

BuildSystem:  python
BuildRequires:  python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

%description
Create functions that efficiently compute the Cyclic Redundancy Check 
(CRC) using table lookup.

Features:

    * Create Python functions for computing the CRC. If the optional 
      extension module is installed, the calculations are preformed 
      using fast C code.
    * Create instances of the Crc class that support the interface 
      used by the md5 and sha modules in the Python standard library.
    * Generate C/C++ code that can be incorporated in another project.
    * Any generator polynomial producing 8, 16, 32, or 64 bit CRCs is 
      allowed.
    * Forward and bit-reverse algorithms are supported.

%build -p
export CFLAGS="%{optflags}"

%files
%doc README
%{python_sitearch}/%{oname}
%{python_sitearch}/%{oname}-%{version}-py%{pyver}.*-info
