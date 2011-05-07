Summary:	A program to send faxes for free via email and the TPC system
Name:		FaxMail
Version:	2.3
Release:	%mkrel 18
License:	GPLv2+
Group:		Networking/Mail
Source0:	ftp://www.inference.phy.cam.ac.uk/pub/www/FaxMail/%{name}-%{version}.tar.bz2
Patch0:		FaxMail-2.3-misc.patch
Patch1:		FaxMail-2.3-fhs.patch
URL: http://www.inference.phy.cam.ac.uk/FaxMail/ 
Requires:	tk >= 4.0
Requires:	tcl >= 7.5
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
make ROOT="%{buildroot}" INSTALLMANPATH=%{_mandir} INSTALLINFOPATH=%{_infodir} FAXMAIL_DIR=%{tcl_sitelib}/%{name} install

%files
%defattr(-,root,root)
%{tcl_sitelib}/%{name}
%{_bindir}/FaxMail
%{_bindir}/tryfax
%{_mandir}/man1/*
%{_infodir}/*
%doc FaxMail.html HISTORY README

%clean
rm -rf %{buildroot}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info
