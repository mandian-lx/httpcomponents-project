%{?_javapackages_macros:%_javapackages_macros}
Name:              httpcomponents-project
Summary:           Common POM file for HttpComponents
Version:           6
Release:           4.1%{?dist}

License:           ASL 2.0
URL:               http://hc.apache.org/
# svn export http://svn.apache.org/repos/asf/httpcomponents/project/tags/%{version} %{name}-%{version}
# tar cJf %{name}-%{version}.tar.xz %{name}-%{version}
Source:            %{name}-%{version}.tar.bz2
BuildArch:         noarch

BuildRequires:     maven-local


%description
Common Maven POM  file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

%prep
%setup -q
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-notice-plugin
%pom_xpath_remove pom:modules

%build
%mvn_file  : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 6-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 6-2
- Build with xmvn

* Mon Aug  6 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 6-1
- Update to upstream version 6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 17 2011 Alexander Kurtakov <akurtako@redhat.com> 4.1.1-3
- Require maven (version 3) now.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.1.1-1
- Initial version
