%global gitdate 20210311

Name:		mikktspace
# Version from .c file
Version:	1.0
Release:	2.git%{gitdate}
URL:		http://www.mikktspace.com/
# git clone https://github.com/mmikk/MikkTSpace.git
# tar --exclude-vcs -cvzf mikktspace-1.0-20210311.tar.gz MikkTSpace
Source0:	mikktspace-%{version}-%{gitdate}.tar.gz
Source1:	CMakeLists.txt
License:	zlib
Summary:	A library to produce normal maps with tangent space
BuildRequires:	gcc, make, cmake

%description
A common standard for tangent space used in baking tools to produce normal
maps.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for mikktspace

%description devel
Development files for mikktspace.

%prep
%setup -q -n MikkTSpace

cp %{SOURCE1} .
%cmake

%build
%cmake_build -- CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_includedir}/mikkelsen/
install -m0644 mikktspace.h %{buildroot}%{_includedir}/mikkelsen/
mkdir -p %{buildroot}%{_libdir}
install -m0755  x86_64-redhat-linux-gnu/libmikktspace.so* %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
	ldconfig -v -n .
	ln -s libmikktspace.so libmikktspace.so.1
popd

%files
%{_libdir}/libmikktspace.so.*

%files devel
%{_includedir}/mikkelsen/
%{_libdir}/libmikktspace.so
%{_libdir}/libmikktspace.so.1

%changelog
* Mon May 31 2021 Roddie Kieley <rkieley@apache.org> - 1.0-2.git20210311
- Now with CmakeLists.txt and hacked up for locally working f34 GA

* Thu Mar 11 2021 Tom Callaway <spot@fedoraproject.org> - 1.0-1.git20210311
- initial package
