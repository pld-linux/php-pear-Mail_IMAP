%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	IMAP
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		subver RC2
%define		rel 5
Summary:	%{_pearname} - a c-client webmail backend
Summary(pl.UTF-8):	%{_pearname} - backend webmaila oparty o bibliotekę c-client
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	0.%{subver}.%{rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	5ed47847db2ff6e5ff733f2bd2147bef
URL:		http://pear.php.net/package/Mail_IMAP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-imap
Requires:	php-pear
Suggests:	php-pear-Net_URL
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Net/URL.*)'

%description
Mail_IMAP provides a simplifed backend for working with the c-client
(IMAP) extension. It serves as an OO wrapper for commonly used
c-client functions. It provides structure and header parsing as well
as body retrieval.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Mail_IMAP dostarcza uproszczonego backendu do pracy z rozszerzeniem
IMAP. Działa jako zorientowany obiektowo wrapper na często używane
funkcje biblioteki c-client. Przetwarza struktury oraz nagłówki jak
również umożliwia odbiór treści wiadomości.

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
