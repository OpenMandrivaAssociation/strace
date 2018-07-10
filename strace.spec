%global _disable_rebuild_configure 1

Name:		strace
Version:	4.22
Release:	2
Summary:	Tracks and displays system calls associated with a running process
License:	BSD
Group:		Development/Kernel
URL:		http://strace.io/
Source0:	https://github.com/strace/strace/archive/v%{version}.tar.gz
Source1:	git-version-gen
Patch0:		strace-4.22-linkage.patch
BuildRequires:	time
BuildRequires:	m4 automake autoconf
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
./bootstrap
%configure
%make

%install
%makeinstall_std

# remove unpackaged files
rm %{buildroot}%{_bindir}/strace-graph
# remove INSTALL file
rm INSTALL

%files
%doc COPYING README* NEWS
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/strace*.1*
