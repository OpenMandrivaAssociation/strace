%define name	strace
%define version	4.5.15
%define	rel	1
%define release	%mkrel %{rel}
#define cvsdate	20050803

Summary:	Tracks and displays system calls associated with a running process
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Development/Kernel
URL:		http://www.liacs.nl/~wichert/strace/
Source0:	%{name}-%{version}%{?cvsdate:-%{cvsdate}}.tar.bz2
Source1:	%{name}.bash-completion
Patch0:		strace-newsysc.patch
Patch1:		strace-getdents64.patch
Patch2:		strace-kernel26_userspace.patch
Patch3:		strace-stat64.patch
Patch4:		strace-sparc64.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1 -b .newsysc
%patch1 -p1 -b .getdents64
%patch2 -p1 -b .kernel26
%patch3 -p1 -b .stat64
%patch4 -p1 -b .sparc64

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

# remove unpackaged files
rm -f %{buildroot}%{_bindir}/strace-graph

# bash completion
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT README* CREDITS ChangeLog INSTALL NEWS PORTING TODO
%{_sysconfdir}/bash_completion.d/%{name}
%{_bindir}/strace
%{_mandir}/man1/strace.1*


