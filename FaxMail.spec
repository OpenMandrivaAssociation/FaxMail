Summary:	A program to send faxes for free via email and the TPC system
Name:		FaxMail
Version:	2.3
Release:	20
License:	GPLv2+
Group:		Networking/Mail
Source0:	ftp://www.inference.phy.cam.ac.uk/pub/www/FaxMail/%{name}-%{version}.tar.bz2
Patch0:		FaxMail-2.3-misc.patch
Patch1:		FaxMail-2.3-fhs.patch
URL: http://www.inference.phy.cam.ac.uk/FaxMail/ 
Requires:	tk >= 4.0
Requires:	tcl >= 7.5
BuildRequires:	tcl-devel
BuildRequires:	tk

%description
This package contains FaxMail, a utility to assist in preparing and
sending faxes via the internet's Email-Fax gateway.  It does this
via the TPC.INT service.  See http://www.tpc.int/ for details.

%prep
%setup -q
%patch0 -p1 -b .misc 
%patch1 -p1 -b .fhs
     
%build
make FAXMAIL_DIR=%{tcl_sitelib}/%{name} CC="cc %optflags %ldflags"

%install
make ROOT="%{buildroot}" INSTALLMANPATH=%{_mandir} INSTALLINFOPATH=%{_infodir} FAXMAIL_DIR=%{tcl_sitelib}/%{name} install

%files
%defattr(-,root,root)
%{tcl_sitelib}/%{name}
%{_bindir}/FaxMail
%{_bindir}/tryfax
%{_mandir}/man1/*
%{_infodir}/*
%doc FaxMail.html HISTORY README


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3-18mdv2011.0
+ Revision: 671963
- mass rebuild

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 2.3-17mdv2011.0
+ Revision: 623262
- use our own build flag

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-17mdv2010.1
+ Revision: 521827
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3-16mdv2010.0
+ Revision: 413005
- rebuild

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 2.3-15mdv2009.1
+ Revision: 310898
- buildrequires tcl-devel (for macros)
- clean requires some more
- don't package COPYING
- new license policy
- move to new locations per policy
- unzip patches
- clean spec

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.3-14mdv2009.0
+ Revision: 220767
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.3-13mdv2008.1
+ Revision: 149714
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 23 2007 Christiaan Welvaart <spturtle@mandriva.org> 2.3-12mdv2008.0
+ Revision: 30050
- Import FaxMail



* Fri Jul 07 2006 Stew Benedict <sbenedict@mandriva.com> 2.3-12mdv2007.0
- rebuild

* Fri Jun 03 2005 Stew Benedict <sbenedict@mandriva.com> 2.3-11mdk
- rebuild

* Fri May 14 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.3-10mdk
- rebuild, update URLs, rpmlint/FHS (patch1)

* Mon Apr 28 2003 Stew Benedict <sbenedict@mandrakesoft.com> 2.3-9mdk
- distriblint

* Mon Dec 30 2002 Stew Benedict <sbenedict@mandrakesoft.com> 2.3-8mdk
- rebuild for new glibc/rpm, remove unused patch1

* Tue Jul 24 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.3-7mdk
- Don't obsolete itself
- s/Copyright/License

* Mon May 21 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 2.3-6mdk
- BuildRequires: tk

* Mon Oct  2 2000 Vincent Saugey <vince@mandrakesoft.com> 2.3-5mdk
- carroect packager flag

* Thu Aug 24 2000 Vincent Saugey <vince@mandrakesoft.com> 2.3-4mdk
- Install info

* Fri Jul 28 2000 Vincent Saugey <vince@mandrakesoft.com> 2.3-3mdk
- BM, Macros

* Wed Apr 05 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.3-2mdk
- updated groups to correct group names.

* Thu Feb 17 2000 Stefan van der Eijk <s.vandereijk@chello.nl>
- removed if statement in .spec file. Mandrake always has libresolv
 
* Mon Nov 23 1998 Matt Davey <mcdavey@mrao.cam.ac.uk>
- Upgraded to FaxMail-2.3
- Changed SRPM according to RHCN Package Requirements      
