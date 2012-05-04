%define	rbname cucumber

Summary:	Behaviour Driven Development with elegance and joy
Name:		rubygem-%{rbname}

Version:	1.1.4
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://cukes.info
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Behaviour Driven Development with elegance and joy.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(examples|features|fixtures|gem_tasks|legacy_features|spec)/'

%install
%gem_install

%files
%{_bindir}/cucumber
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/cucumber
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features/.cucumber
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/fixtures
%{ruby_gemdir}/gems/%{rbname}-%{version}/fixtures/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks
%{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/*.rake
%{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/*.txt
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/legacy_features
%{ruby_gemdir}/gems/%{rbname}-%{version}/legacy_features/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/cucumber
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/yard/
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/yard/default
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/yard/default/layout/
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/yard/default/layout/html/
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/cucumber/*
%{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/yard/default/layout/html/*
%{ruby_gemdir}/gems/%{rbname}-%{version}/gem_tasks/stats
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/.cucumber/stepdefs.json
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*
