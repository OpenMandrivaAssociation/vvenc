%define libname %mklibname vvenc
%define devname %mklibname -d vvenc

Name:           vvenc
Version:        1.8.0
Release:        1
Summary:        Fraunhofer Versatile Video Encoder (VVenC)
License:        BSD-3-Clause-Clear
URL:            https://www.hhi.fraunhofer.de/en/departments/vca/technologies-and-solutions/h266-vvc.html
Source:         https://github.com/fraunhoferhhi/vvenc/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         https://patch-diff.githubusercontent.com/raw/fraunhoferhhi/vvenc/pull/265.patch

BuildRequires:  cmake
Provides:       h266
Provides:       vvc

%description
A fast and efficient H.266/VVC encoder implementation.

%package -n %{libname}
Summary:        Fraunhofer Versatile Video Encoder (VVenC)
Group:          System/Libraries

%description -n %{libname}
A fast and efficient H.266/VVC encoder implementation.

This package contains a library that can other apps use to utilize the
encoding capabilities.

%package -n %{devname}
Summary:        Fraunhofer Versatile Video Encoder (VVenC)
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description -n %{devname}
A fast and efficient H.266/VVC encoder implementation.

This package contains the development files.

%prep
%autosetup -p1

%build
%cmake \
  -DVVENC_ENABLE_THIRDPARTY_JSON=OFF \
  -DCMAKE_SKIP_RPATH=YES \
  -DVVENC_INSTALL_FULLFEATURE_APP=ON

%make_build

%install
%make_install -C build

%files
%license LICENSE.txt
%doc changelog.txt README.md
%{_bindir}/vvencFFapp
%{_bindir}/vvencapp

%files -n %{libname}
%{_libdir}/*.so

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{lname}.pc
%{_libdir}/cmake/%{name}/
