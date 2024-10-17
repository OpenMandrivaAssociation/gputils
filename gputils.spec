%define major %(echo %{version}|cut -d. -f1-2).0

Name:           gputils
Version:        1.5.2
Release:	1
Summary:        A collection of tools for the Microchip (TM) PIC microcontrollers
Source0:        http://sourceforge.net/projects/gputils/files/%{name}/%{major}/%{name}-%{version}.tar.gz
License:        GPLv2+
Group:          Development/Other
Url:            https://gputils.sourceforge.net/

%description
GPUTILS is a collection of tools for the Microchip (TM) PIC microcontrollers.
It includes gpasm, gplink, and gplib.

%prep
%autosetup -p1
autoreconf -fis

%conf
%configure

%build
%make_build

%install
%make_install
%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%doc README
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%{_bindir}/*
%doc %{_docdir}/%{name}-%{version}
