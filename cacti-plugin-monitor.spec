%define		namesrc	monitor
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Monitor
Summary(pl):	Wtyczka do Cacti - Monitor
Name:		cacti-plugin-monitor
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#!!!!problem with version
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	cb88792d17397c340dbdd2eccfa36861
URL:		http://www.cactiusers.org/
#BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti.

%description -l pl
Wtyczka do Cacti.

%prep
%setup -q -n %{namesrc}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  README
%{webcactipluginroot}
