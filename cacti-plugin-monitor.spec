%define		plugin	monitor
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Monitor
Summary(pl.UTF-8):	Wtyczka do Cacti - Monitor
Name:		cacti-plugin-monitor
Version:	0.8.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.zip
# Source0-md5:	c3ce79679e7ae2e6a1d91a294dade776
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
BuildRequires:	unzip
Requires:	cacti
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
