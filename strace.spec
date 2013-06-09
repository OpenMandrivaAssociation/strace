Name:		strace
Version:	4.8
Release:	1
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


%changelog
* Wed Mar 16 2011 Oden Eriksson <oeriksson@mandriva.com> 4.6-1mdv2011.0
+ Revision: 645641
- 4.6
- rediffed P5

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 4.5.20-2mdv2011.0
+ Revision: 607754
- rebuild

* Mon May 17 2010 Eugeni Dodonov <eugeni@mandriva.com> 4.5.20-1mdv2010.1
+ Revision: 544966
- Updated to 4.5.20.
  Dropped merged patches.

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 4.5.19-2mdv2010.1
+ Revision: 519093
- P6: fix build (debian)
- rebuild

* Fri Oct 23 2009 Eugeni Dodonov <eugeni@mandriva.com> 4.5.19-1mdv2010.0
+ Revision: 459011
- Updated to 4.5.19.
  Drop patches 6,7,8,9 (integrated upstream).

* Mon Sep 28 2009 Olivier Blin <oblin@mandriva.com> 4.5.18-4mdv2010.0
+ Revision: 450366
- fix arm eabi (from Arnaud Patard, patch from upstream)

* Mon May 25 2009 Eugeni Dodonov <eugeni@mandriva.com> 4.5.18-3mdv2010.0
+ Revision: 379552
- Fixed off-by-one memory allocation error in util.c (#51181).

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.5.18-2mdv2009.1
+ Revision: 337175
- keep bash completion in its own package

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 4.5.18-1mdv2009.1
+ Revision: 317635
- 4.5.18
- drop upstream implemented patches (P0,P1)
- rediffed some fuzzy patches
- fix build with -Werror=format-security (P6)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 4.5.16-3mdv2009.0
+ Revision: 225504
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Frederic Crozat <fcrozat@mandriva.com> 4.5.16-2mdv2008.1
+ Revision: 121734
- Patch5 : add verbose output for usbdevfs

* Sat Nov 10 2007 David Walluck <walluck@mandriva.org> 4.5.16-1mdv2008.1
+ Revision: 107364
- 4.5.16
- update URL

* Tue May 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.5.15-2mdv2008.0
+ Revision: 29893
- small completion fix


* Thu Jan 25 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 4.5.15-1mdv2007.0
+ Revision: 113407
- new release: 4.5.16

* Sun Jan 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.5.14-3mdv2007.1
+ Revision: 108816
- uncompress all patches
- add bash completion
- Import strace

* Sat Jun 10 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 4.5.14-2mdv2007.0
- add fixes from PLD, will now build on sparc64 :)

* Tue Jan 17 2006 Stefan van der Eijk <stefan@eijk.nu> 4.5.14-1mdk
- 4.5.14

* Fri Aug 19 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 4.5.13-1mdk
- 4.5.13:
  * better x86_64 support for ia32 processes
  * better printing for linux aoi syscalls
  * update ppc syscalls
  * other bug fixes: statfs64, socket options (setsockopt, ipv6, 64-bit), etc.

* Sun Apr 17 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.5.11-1mdk
- 4.5.11
- %%mrel

* Fri Dec 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.5.8-1mdk
- 4.5.8
- fix summary-ended-with-dot

* Tue Jun 29 2004 Stefan van der Eijk <stefan@mandrake.org> 4.5.5-1mdk
- 4.5.5

* Wed Apr 07 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.5.2-1mdk
- new release

