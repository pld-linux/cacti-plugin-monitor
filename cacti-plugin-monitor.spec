%define		namesrc	monitor
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Monitor
Summary(pl.UTF-8):	Wtyczka do Cacti - Monitor
Name:		cacti-plugin-monitor
Version:	0.8.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{namesrc}-%{version}.zip
# Source0-md5:	72d226f568abce60775806c72e504f96
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

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
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
