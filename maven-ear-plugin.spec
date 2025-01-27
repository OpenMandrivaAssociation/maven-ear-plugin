%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-ear-plugin
Version:        2.8
Release:        7.3
Summary:        Maven EAR Plugin
Group:		Development/Java

License:        ASL 2.0
URL:            https://maven.apache.org/plugins/maven-ear-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-archiver
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-annotations
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-verifier
BuildRequires: maven-surefire-plugin
BuildRequires: plexus-archiver
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-utils
BuildRequires: xmlunit

Requires:       maven
Requires:       java
Requires:       jpackage-utils
Requires:       maven-plugin-annotations
Requires:       plexus-archiver
Requires:       plexus-containers-container-default
Requires:       plexus-utils

Obsoletes: maven2-plugin-ear <= 0:2.0.8
Provides: maven2-plugin-ear = 0:%{version}-%{release}

%description
Generates a J2EE Enterprise Archive (EAR) file.

%package javadoc

Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q 

# Was missing
%pom_add_dep org.codehaus.plexus:plexus-container-default:1.0

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.8-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec 13 2012 Tomas Radej <tradej@redhat.com> - 2.8-2
- Forgot to add sources
- Fixed changelog

* Thu Dec 13 2012 Tomas Radej <tradej@redhat.com> - 2.8-1
- Updated to latest upstream

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-3
- Don't use legacy plexus-container-default, resolves: rhbz#878557
- Install license files, resolves: rhbz#880268


* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Tomas Radej <tradej@redhat.com> - 2.7-1
- Updated to latest upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Tomas Radej <tradej@redhat.com> - 2.6-1
- Update to 2.6
- Guideline fixes

* Wed May 18 2011 Alexander Kurtakov <akurtako@redhat.com> 2.5-1
- Update to upstream 2.5 version.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 07 2010 Hui Wang <huwang@redhat.com> - 2.4.2-2
- Added missing requires

* Mon May 31 2010 Hui Wang <huwang@redhat.com> - 2.4.2-1
- Initial version of the package
