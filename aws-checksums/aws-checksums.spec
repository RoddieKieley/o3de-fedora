%global commit 267ac982b4afc7d70b9429c57c31b35f8c96f79a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		aws-checksums
Version:	0.1.10
Release:	2.git%{shortcommit}%{?dist}
Summary:	HW accelerated CRC32c/CRC32 with fallback to efficient SW implementations
URL:		https://github.com/awslabs/aws-checksums
Source0:	https://github.com/awslabs/aws-checksums/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License:	ASL 2.0
BuildRequires:	cmake, make, gcc
BuildRequires:	aws-c-common-devel

%description
Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW
implementations. C interface with language bindings for each of our SDKs.

%package devel
Summary:	Development files for aws-checksums
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	aws-c-common-devel

%description devel
Development files for aws-checksums.

%prep
%autosetup -n %{name}-%{commit}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_SYSTEM_NAME:STRING=Linux -DCMAKE_SIZEOF_VOID_P=8 -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%check
%if 0
%ctest
%endif

%files
%license LICENSE
%doc README.md
%{_usr}/lib/libaws-checksums.so.1*

%files devel
%{_includedir}/aws/checksums/
%{_usr}/lib/aws-checksums/
%{_usr}/lib/libaws-checksums.so

%changelog
* Thu May 27 2021 Roddie Kieley <rkieley@apache.org> - 0.1.10-2.git267ac98
- updated to build on f34 GA

* Wed Mar 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.1.10-1.git267ac98
- initial package
