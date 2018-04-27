%define upstream_name    B-Hooks-EndOfScope
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Execute code after a scope finished compilation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/B/B-Hooks-EndOfScope-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
