%define upstream_name    B-Hooks-EndOfScope

Name:		perl-%{upstream_name}
Version:	0.28
Release:	1

Summary:	Execute code after a scope finished compilation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/B::Hooks::EndOfScope
Source0:	http://www.cpan.org/modules/by-module/B/B-Hooks-EndOfScope-%{version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Sub::Exporter::Progressive)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Variable::Magic)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
