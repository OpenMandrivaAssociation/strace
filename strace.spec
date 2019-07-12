%global _disable_rebuild_configure 1

Name:		strace
Version:	5.2
Release:	1
Summary:	Tracks and displays system calls associated with a running process
License:	BSD
Group:		Development/Kernel
URL:		http://strace.io/
Source0:	https://github.com/strace/strace/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:	git-version-gen
BuildRequires:	time
BuildRequires:	pkgconfig(liblzma)

%description
The strace program intercepts and records the system calls called
and received by a running process.  Strace can print a record of
each system call, its arguments and its return value.  Strace is useful
for diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%prep
%autosetup -p1
install -m755 %{SOURCE1} .

%build
#export CC=gcc
#export CXX=g++

%configure --enable-mpers=check
%make_build

%install
%make_install

# remove unpackaged files
rm %{buildroot}%{_bindir}/strace-graph
# remove INSTALL file
rm INSTALL

%files
%doc COPYING README* NEWS
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/strace*.1*
