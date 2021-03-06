# Do not use %{_libdir} because it's /usr/lib64 on x86_64 boxes
%define LIB_DIR /usr/lib

Summary: ForgeUpgrade helps developer to upgrades their application data
Name: forgeupgrade
Version: @@VERSION@@
Release: 1%{?dist}
BuildArch: noarch
License: LGPL
Group: Development/Tools
URL: https://github.com/Enalean/ForgeUpgrade
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ForgeUpgrade is an application data (files or databases) upgrade automation
tool. It is very close to Ruby on Rails 'migration' system.


%prep
%setup -q

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT

# Application
%{__install} -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__cp} forgeupgrade.php $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__cp} generator.php $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__cp} -r src $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__cp} -r lib $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__cp} -r db $RPM_BUILD_ROOT/%{_datadir}/%{name}

# Should be delivered from Codendi itself
%{__install} -m 755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/dbdriver
%{__cp} examples/CustomDrivers/ForgeUpgrade_Db_Driver_Codendi.php $RPM_BUILD_ROOT/%{_datadir}/%{name}/dbdriver

# Binaries
%{__install} -m 755 -d $RPM_BUILD_ROOT/%{LIB_DIR}/%{name}/bin
%{__install} -m 755 %{name} $RPM_BUILD_ROOT/%{LIB_DIR}/%{name}/bin


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING README.markdown VERSION
%{_datadir}/%{name}
%dir %{LIB_DIR}/%{name}
%dir %{LIB_DIR}/%{name}/bin
%attr(755,root,root) %{LIB_DIR}/%{name}/bin/%{name}
