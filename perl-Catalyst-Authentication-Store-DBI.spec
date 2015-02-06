%define upstream_name    Catalyst-Authentication-Store-DBI
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	User object representing a
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Model::DBI)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildArch:	noarch

%description
This module implements the the Catalyst::Authentication manpage API using
the Catalyst::Model::DBI manpage.

It uses DBI to let your application authenticate users against a database
and it provides support for the Catalyst::Plugin::Authorization::Roles
manpage.

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
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 654884
- rebuild for updated spec-helper

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 408922
- rebuild using %%perl_convert_version

* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 0.01-1mdv2010.0
+ Revision: 397949
- import perl-Catalyst-Authentication-Store-DBI


* Sun Jul 19 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

