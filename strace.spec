Name:		strace
Version:	4.12
Release:	1
Summary:	Tracks and displays system calls associated with a running process
License:	BSD
Group:		Development/Kernel
URL:		http://sourceforge.net/projects/%{name}/
Source0:	http://downloads.sourceforge.net/project/strace/strace/%{version}/%{name}-%{version}.tar.xz
Source1:	git-version-gen
BuildRequires:	time
%ifarch x86_64
# for experimental -k option
BuildRequires:	pkgconfig(libunwind)
%endif

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

%prep
%setup -q
%apply_patches
install -m755 %{SOURCE1} .

%build
%configure
%make

%install
%makeinstall_std

# remove unpackaged files
rm %{buildroot}%{_bindir}/strace-graph
# remove INSTALL file
rm INSTALL

%files
%doc COPYING README* CREDITS NEWS
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/strace.1*
