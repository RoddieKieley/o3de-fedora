Name:		aws-c-io
Version:	0.9.2
Release:	2%{?dist}
Summary:	IO and TLS work for the AWS SDK for C
URL:		https://github.com/awslabs/aws-c-io
Source0:	https://github.com/awslabs/aws-c-io/archive/v%{version}.tar.gz
License:	ASL 2.0
BuildRequires:	cmake, make, gcc
BuildRequires:	s2n-tls-devel, aws-c-common-devel, aws-c-cal-devel
BuildRequires:	openssl-devel

%description
This is a module for the AWS SDK for C. It handles all IO and TLS work for
application protocols. aws-c-io is an event driven framework for implementing
application protocols. It is built on top of cross-platform abstractions that
allow you as a developer to think only about the state machine and API for
your protocols. A typical use-case would be to write something like Http on
top of asynchronous-io with TLS already baked in. All of the platform and
security concerns are already handled for you.

It is designed to be light-weight, fast, portable, and flexible for multiple
domain use-cases such as: embedded, server, client, and mobile.

%package devel
Summary:	Development files for aws-c-io
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	s2n-tls-devel, aws-c-common-devel, aws-c-cal-devel
Requires:	openssl-devel

%description devel
Development files for aws-c-io.

%prep
%setup -q

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_C_FLAGS:STRING=-w -DCMAKE_CXX_FLAGS:STRING=-w -DCMAKE_SYSTEM_NAME:STRING=Linux -DCMAKE_SIZEOF_VOID_P=8 -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%check
%if 0
%ctest
%endif

%files
%license LICENSE NOTICE
%doc README.md
%{_usr}/lib/libaws-c-io.so.1*

%files devel
%{_includedir}/aws/io/
%{_includedir}/aws/testing/io_testing_channel.h
%{_usr}/lib/aws-c-io/
%{_usr}/lib/libaws-c-io.so

%changelog
* Thu May 27 2021 Roddie Kieley <rkieley@apache.org> - 0.9.2-2
- added cmake defines on the cli and ensured lib usage would work

* Wed Mar 17 2021 Tom Callaway <spot@fedoraproject.org> - 0.9.2-1
- initial package
