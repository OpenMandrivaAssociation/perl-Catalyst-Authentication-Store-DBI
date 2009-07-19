
%define realname   Catalyst-Authentication-Store-DBI
%define version    0.01
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    User object representing a
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Catalyst::Model::DBI)
BuildRequires: perl(Catalyst::Plugin::Authentication)

BuildArch: noarch

%description
This module implements the the Catalyst::Authentication manpage API using
the Catalyst::Model::DBI manpage.

It uses DBI to let your application authenticate users against a database
and it provides support for the Catalyst::Plugin::Authorization::Roles
manpage.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


