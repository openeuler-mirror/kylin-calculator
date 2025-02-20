Name:           kylin-calculator
Version:        1.1.0
Release:        3
Summary:        Calculator tool for UKUI
License:        LGPL-3.0-or-later and GPL-3.0-or-later
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz
Patch01:        0001-update-kylin-calculator.desktop.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  pkgconf
BuildRequires:  gsl-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  ukui-interface
BuildRequires:  gmp-devel
BuildRequires:  libkysdk-kabase-devel

# Requires: NetworkManager

%description
Calculator is a lightweight calculator based on
QT5 development, can provide scientific calculation
and exchange rate conversion and other calculation
modes, with simple to use, friendly interface
and other advantages.

%prep
%setup -q
%patch01 -p1

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  kylin-calculator.pro
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/usr/share/doc/kylin-calculator/
mkdir -p %{buildroot}/usr/share/man/man1/
mkdir -p %{buildroot}/usr/share/pixmaps/
cp image/calc.png %{buildroot}/usr/share/pixmaps/
cp debian/copyright  %{buildroot}/usr/share/doc/kylin-calculator/
gzip -c debian/changelog > %{buildroot}/usr/share/doc/kylin-calculator/changelog.gz
gzip -c man/kylin-calculator.1	> %{buildroot}/usr/share/man/man1/kylin-calculator.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/kylin-calculator
%{_datadir}/applications/kylin-calculator.desktop
%{_datadir}/doc/kylin-calculator/changelog.gz
%{_datadir}/doc/kylin-calculator/copyright
%{_datadir}/man/man1/kylin-calculator.1.gz
%{_datadir}/pixmaps/calc.png
%{_datadir}/glib-2.0/schemas/org.kylin-calculator-data.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.log4qt.kylin-calculator.gschema.xml
%{_datadir}/kylin-calculator/translations/kylin-calculator_zh_CN.qm
%{_datadir}/kylin-calculator/translations/kylin-calculator_bo_CN.qm
%{_datadir}/kylin-user-guide/data/guide/kylin-calculator/*

%changelog
* Wed Jun 14 2023 peijiankang <peijiankang@kylinos.cn> - 1.1.0-3
- Type:bugfix
- CVE:
- SUG:NA
- DESC: update kylin-calculator.desktop

* Mon Jan 30 2023 peijiankang <peijiankang@kylinos.cn> - 1.1.0-2
- add debugsource and debuginfo

* Mon Oct 24 2022 tanyulong <tanyulong@kylinos.cn> - 1.1.0-1
- update upstream version 1.1.0

* Tue Sep 27 2022 lvfei <lvfei@kylinos.cn> - 1.0.34-4
- Type:bugfix
- CVE:
- SUG:NA
- DESC: add patch:0001-update-desktop-file-and-add-sdk-translate.patch

* Fri Sep 9 2022 lvfei <lvfei@kylinos.cn> - 1.0.34-3
- Type:bugfix
- CVE:
- SUG:NA
- DESC: add patch:0001-add-and-update-some-zangwen-translate.patch

* Wed May 18 2022 tanyulong <tanyulong@kylinos.cn> - 1.0.34-2
- Improve the project according to the requirements of compliance improvement

* Tue Mar 01 2022 tanyulong <tanyulong@kylinos.cn> - 1.0.34-1
- update upstream to version 1.0.34-1

* Tue Dec 7 2021 douyan <douyan@kylinos.cn> - 1.0.26-2
- fix exchange rate display error

* Tue Dec 7 2021 douyan <douyan@kylinos.cn> - 1.0.26-1
- update to upstream version 1.0.26

* Thu Oct 28 2021 douyan <douyan@kylinos.cn> - 1.0.25-2
- fix switch translation issue

* Wed Oct 27 2021 tanyulong <tanyulong@kylinos.cn> - 1.0.25-1
- update to upstream version 1.0.25

* Tue Oct 26 2021 douyan <douyan@kylinos.cn> - 1.0.1-1
- update to upstream version 1.0.1

* Tue Dec 15 2020 lvhan <lvhan@kylinos.cn> - 1.0.0-1
- update to upstream version 1.0.0
