Summary:            Supporting services and utilities for zRAM compressed memory
Name:               zram-utils
Version:            0.1
Release:            21%{?dist}
License:            Unlicense
Group:              System Environment/Base
Source:             %{name}-%{version}.tar.gz
#URL:                
BuildArch:          noarch       
#BuildRequires:      

%description
zram-utils allows to setup compressed zRAM swap and monitor it.

%prep
%autosetup

%build

%install
env DESTDIR=%{buildroot} ./setup install

#%find_lang %{name}

%files
%doc README.md LICENSE
%{_bindir}/*
%{_libexecdir}/*
%{_unitdir}/*

%preun
/usr/bin/systemctl stop zram.service
/usr/bin/systemctl disable zram.service

%changelog
* Tue Nov 18 2014 Igor Bukanov <igor@mir2.org> 0.1
- initial version
