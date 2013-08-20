Name: libshadowutils
Version: 0.0.1
Release: 1
Summary: Functions from Shadow Tool Suite as shared library
Group: System Environment/Libraries
License: BSD
URL: https://github.com/nemomobile/libshadowutils
Source: %{name}-%{version}.tar.gz
BuildRequires: cmake

%description
This library contains some useful functions from the Shadow Tool Suite
exposed as shared library to be used by applications not shipped with
the Shadow Tool Suite.

%package devel
Summary: Functions from Shadow Tool Suite as shared library (Development)
Group: Development/Libraries
Requires: %{name}

%description devel
This library contains some useful functions from the Shadow Tool Suite
exposed as shared library to be used by applications not shipped with
the Shadow Tool Suite.

%prep
%setup -q

%build
%cmake .
make

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING README README.shadow
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc COPYING README README.shadow
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*/*.h
