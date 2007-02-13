Summary:	Set of polish messages for ht://Dig
Summary(pl.UTF-8):	Zestaw polskich komunikatów do ht://Dig-a
Name:		htdig_pl
Version:	0.1
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	%{name}-%{version}.tgz
# Source0-md5:	64335a24b165cba6a4a9710905962d8c
Requires:	htdig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/htdig

%description
These are some configuration files that allows ht://Dig search engine
to work in Polish language. Package contains a sample config file,
templates and a sample entry to search web page.

%description -l pl.UTF-8
Pakiet zawiera kilka plików konfiguracyjnych, które umożliwiają
przeszukiwarce ht://Dig na pracę w języku polskim. W skład pakietu
wchodzi przykładowy plik konfiguracyjny, szablony stron oraz
przykładowa strona wejściowa do wyszukiwarki.

%prep
%setup -q -n %{name}

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/htdig_pl.conf
%config(missingok) /home/httpd/html/search_pl.html
/var/lib/htdig/common/*pl.html
