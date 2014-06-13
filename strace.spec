%bcond_without	uclibc

Name:		strace
Version:	4.8
Release:	8
Summary:	Tracks and displays system calls associated with a running process
License:	BSD
Group:		Development/Kernel
URL:		http://sourceforge.net/projects/%{name}/
Source0:	http://switch.dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.xz
# These can be removed on the next version bump
Source1:	git-version-gen
Patch0:		strace-4.8-git-ptrace.patch
Patch1:		strace-4.8-ptrace-glibc-2.19.patch

%track
prog %{name} = {
	url = http://sourceforge.net/projects/strace/
	version = %{version}
	regex = %{name}-(__VER__)\.tar\.xz
}

%description
The strace program intercepts and records the system calls called
and received by a running process.  Strace can print a record of
each system call, its arguments and its return value.  Strace is useful
for diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%package -n	uclibc-%{name}
Summary:	uClibc build of strace
Group:		Development/Kernel

%description -n	uclibc-%{name}
The strace program intercepts and records the system calls called
and received by a running process.  Strace can print a record of
each system call, its arguments and its return value.  Strace is useful
for diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%prep
%setup -q
%patch0 -p1 -b .ptrace~
%patch1 -p1 -b .glibc219~
install -m755 %{SOURCE1} .
autoreconf -fis

%build
CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
mkdir -p bits
ln -sf %{uclibc_root}%{multiarch_includedir}/bits/stat.h bits/stat.h
%uclibc_configure
%make
popd
%endif

mkdir -p glibc
pushd glibc
%configure2_5x
%make
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
rm %{buildroot}%{uclibc_root}%{_bindir}/strace-graph
%endif

%makeinstall_std -C glibc

# remove unpackaged files
rm %{buildroot}%{_bindir}/strace-graph

%files
%doc COPYING README* CREDITS ChangeLog INSTALL NEWS
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/strace.1*
