
%if 0%{?rhel} == 8
%global python3_pkgversion 3.11
%endif

Name:           run-nagios-passive-check-and-submit
Version:        0.1.6
Release:        1%{?dist}
Summary:        Run a Nagios passive check and submit its result via the Nagios CGI
License:        UNKNOWN
URL:            https://github.com/mikegerber/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip

%description
Run a Nagios passive check and submit its result via the Nagios CGI.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files run_nagios

%files -f %{pyproject_files}
%{_bindir}/run-nagios-passive-check-and-submit

%changelog
* Thu Nov 05 2026 Mike Gerber <mike@mike-gerber.de> - 0.1.6-1
- Update to 0.1.6
- Switch to pyproject.toml packaging

* Tue Nov 03 2026 Mike Gerber <mike@mike-gerber.de> - 0.1.5-4
- Rebuild for Fedora 45
- Change Source0 to provide a filename with %name
