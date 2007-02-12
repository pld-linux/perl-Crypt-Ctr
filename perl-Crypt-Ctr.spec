%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Ctr
Summary:	Crypt::Ctr Perl module - encrypt data in Counter Mode
Summary(pl.UTF-8):   Moduł Perla Crypt::Ctr - szyfrujący dane w trybie licznika
Name:		perl-Crypt-Ctr
Version:	0.01
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f5e1192078827c1425ae2d9e527211b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Crypt-CFB
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic Counter Mode implementation in pure Perl. The Counter Mode
module constructs a stream cipher from a block cipher or cryptographic
hash funtion and returns it as an object. Any block cipher in the
Crypt:: class can be used, as long as it supports the blocksize and
keysize methods. Any hash function in the Digest:: class can be used,
as long as it supports the add method.

%description -l pl.UTF-8
Implementacja ogólnego trybu licznika (Generic Counter Mode) w czystym
Perlu. Moduł ten tworzy strumieniowy szyfr z blokowego szyfru lub
kryptograficznej funkcji mieszającej i zwraca go jako obiekt. Może być
wykorzystany dowolny szyfr blokowy z klasy Crypt::, o ile tylko
obsługuje metody blocksize i keysize. Może być użyta dowolna funkcja
mieszająca z klasy Digest::, o ile tylko obsługuje metodę add.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Crypt/Ctr.pm
%{_mandir}/man3/*
