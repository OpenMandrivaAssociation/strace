Name:		strace
Version:	4.8
Release:	5
Summary:	Tracks and displays system calls associated with a running process
License:	BSD
Group:		Development/Kernel
URL:		http://sourceforge.net/projects/strace/
Source0:	http://switch.dl.sourceforge.net/project/strace/strace/%version/strace-%version.tar.xz

%track
prog %name = {
	url = http://sourceforge.net/projects/strace/
	version = %version
	regex = %name-(__VER__)\.tar\.xz
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

%build
%configure2_5x
%{make}

%install
%makeinstall_std

# remove unpackaged files
%{__rm} %{buildroot}%{_bindir}/strace-graph

%files
%doc COPYING README* CREDITS ChangeLog INSTALL NEWS
%_bindir/strace
%_bindir/strace-log-merge
%_mandir/man1/strace.1*
