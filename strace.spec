Name:		strace
Version:	4.7
Release:	1
Summary:	Tracks and displays system calls associated with a running process
License:	BSD
Group:		Development/Kernel
URL:		http://sourceforge.net/projects/strace/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/strace/strace-%{version}.tar.xz
# (fc) 4.5.16-2mdv display usbdevfs trace
Patch5:		http://iki.fi/lindi/strace-usbdevfs.patch

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
#patch5 -p1 -b .usbdevfs

#needed by patch5
autoreconf

%build
%configure2_5x
%{make}

%install
%makeinstall_std

# remove unpackaged files
%{__rm} %{buildroot}%{_bindir}/strace-graph

%files
%doc COPYRIGHT README* CREDITS ChangeLog NEWS
%{_bindir}/strace*
%{_mandir}/man1/strace.1*
