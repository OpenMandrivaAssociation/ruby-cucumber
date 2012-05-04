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
