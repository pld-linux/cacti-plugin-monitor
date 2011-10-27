%define		plugin	monitor
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - Monitoring for Cacti
Summary(pl.UTF-8):	Wtyczka do Cacti - Monitor
Name:		cacti-plugin-%{plugin}
Version:	1.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:monitor-v%{version}-1.tgz
# Source0-md5:	45a354b05be7eeebb5319c0ddcee2849
URL:		http://docs.cacti.net/plugin:monitor
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.8
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-mysql
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Plugin for Cacti - adds a tab to visually show you the Up/Down Status
of all your hosts. It will audibly alert you whenever a host goes
down.

%description -l pl.UTF-8
Wtyczka do Cacti dodająca zakładkę wizualnie pokazującą stan
(działający/nie działający) wszystkich hostów. Ponadto wtyczka ta
dźwiękowo alarmuje kiedy host przestaje działać.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
