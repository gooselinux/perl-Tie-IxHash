Name:           perl-Tie-IxHash
Version:        1.21
Release:        10.1%{?dist}
Summary:        Ordered associative arrays for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Tie-IxHash/
Source0:        http://www.cpan.org/authors/id/G/GS/GSAR/Tie-IxHash-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This Perl module implements Perl hashes that preserve the order in
which the hash elements were added. The order is not affected when
values corresponding to existing keys in the IxHash are changed.
The elements can also be set to any arbitrary supplied order. The
familiar perl array operations can also be performed on the IxHash.


%prep
%setup -q -n Tie-IxHash-%{version}
chmod -c 644 Changes README


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Tie/
%{_mandir}/man3/*.3pm*


%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.21-10.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.21-8
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.21-7
- rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.21-6.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Sep  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.21-6
- Rebuild for FC6.

* Thu Feb 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.21-5
- Rebuild for FC5 (perl 5.8.8).

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.21-4
- Dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.21-3
- rebuilt

* Sun May  9 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.21-0.fdr.2
- Avoid creation of the perllocal.pod file (make pure_install).

* Thu May  6 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.21-0.fdr.1
- First build.
