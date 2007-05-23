%define name FaxMail
%define version 2.3
%define release %mkrel 12

Summary: A program to send faxes for free via email and the TPC system
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Mail
Source: ftp://www.inference.phy.cam.ac.uk/pub/www/FaxMail/%{name}-%version.tar.bz2
Patch0: FaxMail-2.3-misc.patch.bz2
Patch1: FaxMail-2.3-fhs.patch.bz2
URL: http://www.inference.phy.cam.ac.uk/FaxMail/ 
Requires: tk >= 4.0, tcl >= 7.5
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: tcl, tk

%description
This package contains FaxMail, a utility to assist in preparing and
sending faxes via the internet's Email-Fax gateway.  It does this
via the TPC.INT service.  See http://www.tpc.int/ for details.

%prep
%setup -q
%patch0 -p1 -b .misc 
%patch1 -p1 -b .fhs
     
%build
make 

%install
rm -rf $RPM_BUILD_ROOT
make ROOT="$RPM_BUILD_ROOT" INSTALLMANPATH=%{_mandir} INSTALLINFOPATH=%{_infodir} install

%files
%defattr(-,root,root)
%dir %{_datadir}/FaxMail
%{_datadir}/FaxMail/FaxMail.tcl
%{_datadir}/FaxMail/cover.lst
%{_bindir}/FaxMail
%{_bindir}/tryfax
%{_mandir}/man1/*
%{_infodir}/*
%doc COPYING FaxMail.html HISTORY README

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info
