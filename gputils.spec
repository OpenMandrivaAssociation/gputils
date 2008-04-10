%define name    gputils
%define version 0.13.5
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A collection of tools for the Microchip (TM) PIC microcontrollers
Source0:        %{name}-%{version}.tar.bz2
License:        GPL
Group:          Development/Other
Url:            http://gputils.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GPUTILS is a collection of tools for the Microchip (TM) PIC microcontrollers.
It includes gpasm, gplink, and gplib.

%prep
%setup -q
%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%{_bindir}/*
