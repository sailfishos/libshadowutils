Name: libshadowutils
Version: 0.0.6
Release: 0
Summary: Functions from Shadow Tool Suite as shared library
License: BSD-3-Clause
URL: https://github.com/sailfishos/libshadowutils/
Source: %{name}-%{version}.tar.gz
Patch1: 0001-libshadowutils-Functions-from-Shadow-Tool-Suite-as-s.patch
BuildRequires: cmake

%description
This library contains some useful functions from the Shadow Tool Suite
exposed as shared library to be used by applications not shipped with
the Shadow Tool Suite.

%package devel
Summary: Functions from Shadow Tool Suite as shared library (Development)
Requires: %{name}  = %{version}-%{release}

%description devel
This library contains some useful functions from the Shadow Tool Suite
exposed as shared library to be used by applications not shipped with
the Shadow Tool Suite.

%package doc
Summary:   Documentation for %{name}
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake \
       -DLIBSHADOWUTILS_VERSION=%{version}-%{release} \
       -DLIBSHADOWUTILS_VERSION_SONAME=`echo %{version} | sed 's/\..*//'` .
%cmake_build

%install
%cmake_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}
