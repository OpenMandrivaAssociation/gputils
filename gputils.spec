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
