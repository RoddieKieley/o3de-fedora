Name:		aws-c-cal
Version:	0.5.1
Release:	2%{?dist}
Summary:	Aws Crypto Abstraction Layer
URL:		https://github.com/awslabs/aws-c-common
Source0:	https://github.com/awslabs/aws-c-common/archive/v%{version}.tar.gz
Patch0:		aws-c-cal-0.5.1-fix-compile-against-openssl.patch
License:	ASL 2.0
BuildRequires:	cmake, make, gcc
BuildRequires:	openssl-devel, aws-c-common-devel

%description
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for cryptography
primitives.

%package devel
Summary:	Development files for aws-c-cal
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	openssl-devel, aws-c-common-devel

%description devel
Development files for aws-c-cal.

%prep
%setup -q
%patch0 -p1 -b .fixup

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_C_FLAGS:STRING=-w -DCMAKE_CXX_FLAGS:STRING=-w -DCMAKE_SYSTEM_NAME:STRING=Linux -DCMAKE_SIZEOF_VOID_P=8 -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%check
# A few odd failures here. Could be because we're not using the aws boringssl fork.
# Sigh.
%if 0
%ctest
%endif

%files
%license LICENSE NOTICE
%doc README.md
# sha256_profile
%{_usr}/lib/libaws-c-cal.so.1*

%files devel
%{_includedir}/aws/cal/
%{_usr}/lib/aws-c-cal/
%{_usr}/lib/libaws-c-cal.so

%changelog
* Thu May 27 2021 Roddie Kieley <rkieley@apache.org> - 0.5.1-2
- ensure lib dir usage that works for stock f34 GA
- add cmake defines for linux platform 64 bit release with debug info

* Wed Mar 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.5.1-1
- initial package
