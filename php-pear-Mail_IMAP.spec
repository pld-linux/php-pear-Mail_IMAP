# ToDo:
# - pl summary
%include	/usr/lib/rpm/macros.php
%define         _class          Mail
%define         _subclass       IMAP
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Provides a c-client webmail backend.
#Summary(pl):	%{_pearname} - Dostarcza
Name:		php-pear-%{_pearname}
Version:	0.1.4A
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0e3c559a6bcf55c7748ffaf58993e92e
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail_IMAP provides a simplifed backend for working with the c-client
(IMAP) extension.  It serves as an OO wrapper for commonly used c-client
functions. It provides structure and header parsing as well as body
retrieval.

This class has in PEAR status: %{_status}.

%description -l pl
Mail_IMAP dostarcza uproszczonego back-endu do pracy z rozszerzeniem
IMAP. Dzia�a jako zorientowany obiektowo wrapper na cz�sto u�ywane
funkcje. Przetwarza struktury oraz nag��wki jak r�wnie� umo�liwia odbi�r
tre�ci wiadomo�ci. 

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
