%define name    gputils
%define version 0.13.7
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A collection of tools for the Microchip (TM) PIC microcontrollers
Source0:        http://sourceforge.net/projects/gputils/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:		gputils-0.13.7-fix-str-fmt.patch
License:        GPLv2+
Group:          Development/Other
Url:            http://gputils.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GPUTILS is a collection of tools for the Microchip (TM) PIC microcontrollers.
It includes gpasm, gplink, and gplib.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*
%{_bindir}/*
