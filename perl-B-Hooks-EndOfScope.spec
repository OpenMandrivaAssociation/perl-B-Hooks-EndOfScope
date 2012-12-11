%define upstream_name    B-Hooks-EndOfScope
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Execute code after a scope finished compilation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/B/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
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

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 658518
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 552258
- update to 0.09

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 402062
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 370008
- update to new version 0.08

* Sat Feb 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.1
+ Revision: 343669
- update to new version 0.07

* Wed Jan 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.1
+ Revision: 332121
- update to new version 0.06

* Mon Jan 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 325041
- new version

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 296792
- import perl-B-Hooks-EndOfScope


* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
- initial mdv release, generated with cpan2dist

