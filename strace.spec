Name:		strace
Version:	4.5.18
Release:	%mkrel 4
Summary:	Tracks and displays system calls associated with a running process
License:	BSD
Group:		Development/Kernel
URL:		http://sourceforge.net/projects/strace/
Source0:	http://easynews.dl.sourceforge.net/sourceforge/strace/strace-%{version}.tar.bz2
Patch3:		strace-stat64.patch
# (fc) 4.5.16-2mdv display usbdevfs trace
Patch5:		http://iki.fi/lindi/strace-usbdevfs.patch
Patch6:		strace-4.5.18-format_not_a_string_literal_and_no_format_arguments.diff
Patch7:		strace-4.5.18-printstr.patch
Patch8:		strace_arm_eabi1.patch
Patch9:		strace_arm_eabi2.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
%patch3 -p1 -b .stat64
%patch5 -p1 -b .usbdevfs
%patch6 -p1 -b .format_not_a_string_literal_and_no_format_arguments
%patch7 -p1 -b .printstr
%patch8 -p1 -b .eabi1
%patch9 -p1 -b .eabi2

#needed by patch5
autoreconf

%build
%configure2_5x
%{make}

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

# remove unpackaged files
%{__rm} %{buildroot}%{_bindir}/strace-graph

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT README* CREDITS ChangeLog INSTALL NEWS PORTING TODO
%{_bindir}/strace
%{_mandir}/man1/strace.1*
