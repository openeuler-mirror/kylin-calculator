%define debug_package %{nil}
Name:           kylin-calculator
Version:        1.0.0
Release:        1
Summary:        Calculator tool for UKUI
License:        GPL-3+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  pkgconf
BuildRequires:  gsl-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  gsettings-qt-devel

# Requires: NetworkManager

%description
 Calculator is a lightweight calculator based on
 QT5 development, can provide scientific calculation
 and exchange rate conversion and other calculation
 modes, with simple to use, friendly interface
 and other advantages.

%prep
%setup -q

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  kylin-calculator.pro
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/etc/bin/
cp %{buildroot}/usr/bin/kylin-calculator %{buildroot}/etc/bin
mkdir -p %{buildroot}/usr/share/doc/kylin-calculator/
mkdir -p %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/kylin-calculator/
gzip -c debian/changelog > %{buildroot}/usr/share/doc/kylin-calculator/changelog.gz
gzip -c man/kylin-calculator.1	> %{buildroot}/usr/share/man/man1/kylin-calculator.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/kylin-calculator
%{_sysconfdir}/bin/kylin-calculator
%{_datadir}/applications/kylin-calculator.desktop
%{_datadir}/doc/kylin-calculator/changelog.gz
%{_datadir}/doc/kylin-calculator/copyright
%{_datadir}/man/man1/kylin-calculator.1.gz
%{_datadir}/pixmaps/calc.png

%changelog
* Tue Dec 15 2020 lvhan <lvhan@kylinos.cn> - 1.0.0-1
- update to upstream version 1.0.0
