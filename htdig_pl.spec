Summary:	Set of polish messages for ht://Dig
Summary(pl):	Zestaw polskich komunikatów do ht://Dig-a
Name:		htdig_pl
Version:	0.1
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	%{name}-%{version}.tgz
# Source0-md5:	64335a24b165cba6a4a9710905962d8c
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	htdig

%define		_sysconfdir	/etc/htdig

%description
These are some configuration files that allows ht://Dig search engine
to work in Polish language. Package contains a sample config file,
templates and a sample entry to search web page.

%description -l pl
Pakiet zawiera kilka plików konfiguracyjnych, które umo¿liwiaj±
przeszukiwarce ht://Dig na pracê w jêzyku polskim. W sk³ad pakietu
wchodzi przyk³adowy plik konfiguracyjny, szablony stron oraz
przyk³adowa strona wej¶ciowa do wyszukiwarki.

%prep
%setup -q -n htdig_pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/htdig,var/lib/htdig/common,home/httpd/html}

install custom_pl.html header_pl.html nomatch_pl.html syntax_pl.html \
	footer_pl.html 	$RPM_BUILD_ROOT/var/lib/htdig/common
install search_pl.html 	$RPM_BUILD_ROOT/home/httpd/html
install htdig_pl.conf 	$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config %{_sysconfdir}/htdig_pl.conf
%config(missingok) /home/httpd/html/search_pl.html
/var/lib/htdig/common/*pl.html
