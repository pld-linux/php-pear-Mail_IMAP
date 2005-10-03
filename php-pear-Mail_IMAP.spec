%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	IMAP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - a c-client webmail backend
Summary(pl):	%{_pearname} - backend webmaila oparty o bibliotekê c-client
Name:		php-pear-%{_pearname}
Version:	1.1.0
%define		_rc RC1
%define		_rel 0.2
Release:	0.%{_rc}.%{_rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	62481c4517c0727bedd1acd9c7c8b451
URL:		http://pear.php.net/package/Mail_IMAP/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-imap
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Net/URL.*)'

%description
Mail_IMAP provides a simplifed backend for working with the c-client
(IMAP) extension.  It serves as an OO wrapper for commonly used
c-client functions. It provides structure and header parsing as well
as body retrieval.

In PEAR status of this package is: %{_status}.

%description -l pl
Mail_IMAP dostarcza uproszczonego backendu do pracy z rozszerzeniem
IMAP. Dzia³a jako zorientowany obiektowo wrapper na czêsto u¿ywane
funkcje biblioteki c-client. Przetwarza struktury oraz nag³ówki jak
równie¿ umo¿liwia odbiór tre¶ci wiadomo¶ci.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
