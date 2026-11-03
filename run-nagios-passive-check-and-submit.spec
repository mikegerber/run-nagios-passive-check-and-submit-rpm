%define name run-nagios-passive-check-and-submit
%define version 0.1.5
%define release 3%{?dist}

Summary: Run a Nagios passive check and submit its result via the Nagios CGI
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://github.com/neingeist/%{name}/archive/%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mike Gerber <mike@sprachgewalt.de>

BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: %{py3_dist beautifulsoup4 lxml requests termcolor}
Requires: python3-pyyaml

%description
Run a Nagios passive check and submit its result via the Nagios CGI.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version}

%build
%{python3} setup.py build

%install
%{python3} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# Fedora does not like an unversioned python shebang:
sed -i 's%#!/usr/bin/python$%#!%{python3}%' $RPM_BUILD_ROOT/%{_bindir}/run-nagios-passive-check-and-submit

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
