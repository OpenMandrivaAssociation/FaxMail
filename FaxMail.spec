Summary:	A program to send faxes for free via email and the TPC system
Name:		FaxMail
Version:	2.3
Release:	27
License:	GPLv2+
Group:		Networking/Mail
Url:		http://www.inference.phy.cam.ac.uk/FaxMail/ 
Source0:	ftp://www.inference.phy.cam.ac.uk/pub/www/FaxMail/%{name}-%{version}.tar.bz2
Patch0:		FaxMail-2.3-misc.patch
Patch1:		FaxMail-2.3-fhs.patch

BuildRequires:	pkgconfig(tcl)
BuildRequires:	tk
Requires:	tk >= 4.0
Requires:	tcl >= 7.5

%description
This package contains FaxMail, a utility to assist in preparing and
sending faxes via the internet's Email-Fax gateway.  It does this
via the TPC.INT service.  See http://www.tpc.int/ for details.

%prep
%setup -q
%apply_patches
     
%build
make FAXMAIL_DIR=%{tcl_sitelib}/%{name} CC="cc %optflags %ldflags"

%install
make ROOT="%{buildroot}" INSTALLMANPATH=%{_mandir} INSTALLINFOPATH=%{_infodir} FAXMAIL_DIR=%{tcl_sitelib}/%{name} install

%files
%doc FaxMail.html HISTORY README
%{tcl_sitelib}/%{name}
%{_bindir}/FaxMail
%{_bindir}/tryfax
%{_mandir}/man1/*
%{_infodir}/*

