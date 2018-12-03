Name: libshadowutils
Version: 4.6
Release: 4
Summary: Functions from Shadow Tool Suite as shared library
Group: System Environment/Libraries
License: BSD
URL: https://git.merproject.org/mer-core/libshadowutils/
Source: %{name}-%{version}.tar.gz
Source1: CMakeLists.txt
Source2: README
Source3: libshadowutils.pc.in
Source4: test_getdef.c
Patch1: library.diff
BuildRequires: cmake

%description
This library contains some useful functions from the Shadow Tool Suite
exposed as shared library to be used by applications not shipped with
the Shadow Tool Suite.

%package devel
Summary: Functions from Shadow Tool Suite as shared library (Development)
Group: Development/Libraries
Requires: %{name}  = %{version}-%{release}

%description devel
This library contains some useful functions from the Shadow Tool Suite
exposed as shared library to be used by applications not shipped with
the Shadow Tool Suite.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream
%patch1 -p1
cp %{SOURCE1} %{SOURCE3} %{SOURCE4} .

%build
%cmake -D LIBSHADOWUTILS_VERSION=%{version}-%{release} -D LIBSHADOWUTILS_VERSION_SONAME=`echo %{version} | sed 's/\..*//'` .
make

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
mv -f lib*.so* ${RPM_BUILD_ROOT}%{_libdir}/
mv -f %{name}.pc ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/%{name}
install -D lib/getdef.h ${RPM_BUILD_ROOT}%{_includedir}/%{name}
mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
install -D %{SOURCE2} ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}/
install README ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}/README.shadow

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*/*.h

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
