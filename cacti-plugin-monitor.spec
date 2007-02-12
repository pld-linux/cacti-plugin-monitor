%define		namesrc	monitor
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Monitor
Summary(pl.UTF-8):	Wtyczka do Cacti - Monitor
Name:		cacti-plugin-monitor
Version:	0.7
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://cactiusers.net/downloads/plugins/%{namesrc}-%{version}.tar.gz
# Source0-md5:	f630549cc354236ea140282b1741fb9d
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - adds a tab to visually show you the Up/Down Status
of all your hosts. It will audibly alert you whenever a host goes down. 

%description -l pl.UTF-8
Wtyczka do Cacti dodająca zakładkę wizualnie pokazującą stan
(działający/nie działający) wszystkich hostów. Ponadto wtyczka ta
dźwiękowo alarmuje kiedy host przestaje działać.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
