#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	BigInt-Named
Summary:	Math::BigInt::Named - BigInts that know their name in some languages
Summary(pl.UTF-8):	Math::BigInt::Named - BigInty znające swoje nazwy w niektórych językach
Name:		perl-Math-BigInt-Named
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed4ae17fb2dabfabbe408f24130e483e
URL:		http://search.cpan.org/dist/Math-BigInt-Named/
BuildRequires:	perl-Math-BigInt >= 1.48
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.48
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a subclass of Math::BigInt and adds support for named numbers
in English and German.

%description -l pl.UTF-8
To jest podklasa Math::BigInt dodająca obsługę słownej reprezentacji
liczb w języku angielskim i niemieckim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README TODO
%{perl_vendorlib}/Math/BigInt/Named.pm
%{perl_vendorlib}/Math/BigInt/Named
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
