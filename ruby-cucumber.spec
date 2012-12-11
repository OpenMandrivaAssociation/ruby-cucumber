%define	rbname cucumber

Summary:	Behaviour Driven Development with elegance and joy
Name:		ruby-%{rbname}

Version:	1.1.9
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://cukes.info
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch
%rename		rubygem-%{rbname}

%description
Behaviour Driven Development with elegance and joy.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep

%build

%install
gem install -E --bindir=%{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/cache
find  %{buildroot}%{ruby_gemdir}/ -type f -name '.*' -delete

%files
%{_bindir}/cucumber
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/
%{ruby_gemdir}/gems/%{rbname}-%{version}/cucumber.gemspec
%{ruby_gemdir}/gems/%{rbname}-%{version}/cucumber.yml
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/
%{ruby_gemdir}/gems/%{rbname}-%{version}/fixtures/
%{ruby_gemdir}/gems/%{rbname}-%{version}/Gemfile
%{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/
%{ruby_gemdir}/gems/%{rbname}-%{version}/History.md
%{ruby_gemdir}/gems/%{rbname}-%{version}/legacy_features/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%{ruby_gemdir}/gems/%{rbname}-%{version}/Rakefile
%{ruby_gemdir}/gems/%{rbname}-%{version}/README.md
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*


%changelog
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.9-1
+ Revision: 796005
-update to 1.1.9
- rename
- don't use broken gem_helper
- rename package according to ruby packaging policy

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.4-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.4-1
+ Revision: 766992
- version update 1.1.4

* Wed Sep 07 2011 Andrey Smirnov <asmirnov@mandriva.org> 0.10.3-1
+ Revision: 698635
- rpmlint warning

  + Alexander Barakin <abarakin@mandriva.org>
    - imported package rubygem-cucumber

* Mon Mar 14 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.0-1
+ Revision: 644643
- new release: 0.10.0
- regenerate spec with gem2rpm5

* Wed Dec 01 2010 Rémy Clouard <shikamaru@mandriva.org> 0.9.4-1mdv2011.0
+ Revision: 604513
- bump release now that rspec 2 is in stable version

* Wed Nov 03 2010 Rémy Clouard <shikamaru@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 592898
- import rubygem-cucumber

