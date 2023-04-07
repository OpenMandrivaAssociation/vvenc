%define lname libvvenc
%define __builddir build/release-shared
Name:           vvenc
Version:        1.7.0
Release:        0
Summary:        Fraunhofer Versatile Video Encoder (VVenC)
License:        BSD-3-Clause-Clear
URL:            https://www.hhi.fraunhofer.de/en/departments/vca/technologies-and-solutions/h266-vvc.html
Source:         https://github.com/fraunhoferhhi/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         gcc11-numeric_limits.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.13

%description
A fast and efficient H.266/VVC encoder implementation.

%package -n %{lname}
Summary:        Fraunhofer Versatile Video Encoder (VVenC)
Group:          System/Libraries

%description -n %{lname}
A fast and efficient H.266/VVC encoder implementation.

This package contains a library that can other apps use to utilize the
encoding capabilities.

%package devel
Summary:        Fraunhofer Versatile Video Encoder (VVenC)
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
A fast and efficient H.266/VVC encoder implementation.

This package contains the development files.

%prep
%autosetup -p1

%build
%cmake \
  -DVVENC_ENABLE_THIRDPARTY_JSON=OFF \
  -DCMAKE_SKIP_RPATH=YES \
%{?nil}
%cmake_build

%install
%cmake_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc changelog.txt README.md
%{_bindir}/vvencFFapp
%{_bindir}/vvencapp

%files -n %{lname}
%{_libdir}/*.so

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{lname}.pc
%{_libdir}/cmake/%{name}/
