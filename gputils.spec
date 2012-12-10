%define name    gputils
%define version 0.14.2
%define release 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A collection of tools for the Microchip (TM) PIC microcontrollers
Source0:        http://sourceforge.net/projects/gputils/files/%{name}/%{version}/%{name}-%{version}.tar.gz
License:        GPLv2+
Group:          Development/Other
Url:            http://gputils.sourceforge.net/
Patch0:		gputils-0.14.2-warnonce.patch

%description
GPUTILS is a collection of tools for the Microchip (TM) PIC microcontrollers.
It includes gpasm, gplink, and gplib.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fis
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*
%{_bindir}/*


%changelog
* Mon Jul 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.14.2-1
+ Revision: 809840
- version update 0.14.2

* Thu Jan 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.14.1-1
+ Revision: 760330
- version update 0.14.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.13.7-2mdv2011.0
+ Revision: 610977
- rebuild

* Thu Jan 28 2010 Funda Wang <fwang@mandriva.org> 0.13.7-1mdv2010.1
+ Revision: 497625
- New version 0.13.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Aug 02 2008 Funda Wang <fwang@mandriva.org> 0.13.6-1mdv2009.0
+ Revision: 260692
- New version 0.13.6

* Thu Apr 10 2008 Giuseppe Ghibò <ghibo@mandriva.com> 0.13.5-1mdv2009.0
+ Revision: 192540
- Release 0.13.5.

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.13.4-1mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Couriousous <couriousous@mandriva.org> 0.13.4-1mdv2008.0
+ Revision: 54820
- 0.13.4
- Import gputils

