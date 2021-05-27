Name:		s2n-tls
Version:	1.0.1
Release:	1%{?dist}
Summary:	An implementation of the TLS/SSL protocols
URL:		https://github.com/aws/s2n-tls
Source0:	https://github.com/aws/s2n-tls/archive/v%{version}.tar.gz
Patch0:		s2n-tls-1.0.1-shared-library-versioned.patch
License:	ASL 2.0
BuildRequires:	cmake, make, gcc
BuildRequires:	openssl-devel

%description
s2n-tls is a C99 implementation of the TLS/SSL protocols that is designed to
be simple, small, fast, and with security as a priority. It is released and
licensed under the Apache License 2.0.

%package devel
Summary:	Development files for s2n-tls
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for s2n-tls.

%prep
%setup -q
%patch0 -p1 -b .shared-version

# kinda useful if the shared library doesn't have EVERYTHING HIDDEN
sed -i 's| -fvisibility=hidden -DS2N_EXPORTS||g' CMakeLists.txt

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_C_FLAGS:STRING=-w -DCMAKE_CXX_FLAGS:STRING=-w -DCMAKE_SYSTEM_NAME:STRING=Linux -DCMAKE_SIZEOF_VOID_P=8 -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%check
#for o3de rpm dev
%if 0
%ctest
%endif

%files
%license LICENSE NOTICE
%doc README.md
%{_usr}/lib/libs2n.so.0*

%files devel
%{_includedir}/s2n.h
%{_usr}/lib/libs2n.so
%{_usr}/lib/s2n/

%changelog
* Thu May 27 2021 Roddie Kieley <rkieley@apache.org> - 1.0.1-2
- updated to use non-64bit lib location

* Wed Mar 17 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.1-1
- initial package
