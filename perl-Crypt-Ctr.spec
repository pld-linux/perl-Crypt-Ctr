%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Ctr
Summary:	Crypt::Ctr Perl module - encrypt data in Counter Mode
Summary(pl):	Modu� Perla Crypt::Ctr - szyfruj�cy dane w trybie licznika
Name:		perl-Crypt-Ctr
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
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

%description -l pl
Implementacja og�lnego trybu licznika (Generic Counter Mode) w czystym
Perlu. Modu� ten tworzy strumieniowy szyfr z blokowego szyfru lub
kryptograficznej funkcji mieszaj�cej i zwraca go jako obiekt. Mo�e by�
wykorzystany dowolny szyfr blokowy z klasy Crypt::, o ile tylko
obs�uguje metody blocksize i keysize. Mo�e by� u�yta dowolna funkcja
mieszaj�ca z klasy Digest::, o ile tylko obs�uguje metod� add.

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
