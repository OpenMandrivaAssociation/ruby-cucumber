%define rbname cucumber

Summary:	Behaviour Driven Development with elegance and joy
Name:		ruby-%{rbname}
Version:	1.3.17
Release:	1
License:	GPLv2+ or Ruby
Group:		Development/Ruby
Url:		http://cukes.info
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	locales-en
BuildRequires:	rubygems
BuildArch:	noarch

%description
Behaviour Driven Development with elegance and joy.

%files
%{_bindir}/cucumber
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/bin
%{gem_dir}/gems/%{rbname}-%{version}/bin/cucumber
%dir %{gem_dir}/gems/%{rbname}-%{version}/features
%dir %{gem_dir}/gems/%{rbname}-%{version}/features/.cucumber
%{gem_dir}/gems/%{rbname}-%{version}/features/*
%dir %{gem_dir}/gems/%{rbname}-%{version}/fixtures
%{gem_dir}/gems/%{rbname}-%{version}/fixtures/*
%dir %{gem_dir}/gems/%{rbname}-%{version}/gem_tasks
%{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/*.rake
%{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/*.txt
%dir %{gem_dir}/gems/%{rbname}-%{version}/legacy_features
%{gem_dir}/gems/%{rbname}-%{version}/legacy_features/*
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*
%dir %{gem_dir}/gems/%{rbname}-%{version}/spec
%{gem_dir}/gems/%{rbname}-%{version}/spec/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/spec/cucumber
%dir %{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/yard/
%dir %{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/yard/default
%dir %{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/yard/default/layout/
%dir %{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/yard/default/layout/html/
%{gem_dir}/gems/%{rbname}-%{version}/spec/cucumber/*
%{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/yard/default/layout/html/*
%{gem_dir}/gems/%{rbname}-%{version}/gem_tasks/stats
%{gem_dir}/gems/%{rbname}-%{version}/features/.cucumber/stepdefs.json
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/examples
%{gem_dir}/gems/%{rbname}-%{version}/examples/*

#------------------------------------------------------------------

%prep
%setup -q

%build
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
%gem_build -f '(examples|features|fixtures|gem_tasks|legacy_features|spec)/'

%install
%gem_install

