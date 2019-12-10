%define         pkgname         scrcpy
%global         forgeurl        https://github.com/Genymobile/%{pkgname}
Version:        1.12

%forgemeta -i

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        Display and control your Android device
License:        ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/Genymobile/%{pkgname}/releases/download/v%{version}/%{pkgname}-server-v%{version}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  java-devel >= 8
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)

Requires:       adb

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%prep
%forgesetup

%build
%meson -Db_lto=true -Dprebuilt_server='%{S:1}'
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md DEVELOP.md FAQ.md
%{_bindir}/%{pkgname}
%{_datadir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*

%changelog
* Tue Dec 10 2019 zeno <zeno@bafh.org> 1.12-1
- Bump version to 1.12
* Sun Dec 01 2019 zeno <zeno@bafh.org> 1.11-5
- Use forge macros
* Tue Nov 26 2019 zeno <zeno@bafh.org> 1.11-4
- minor fixes
* Mon Nov 25 2019 zeno <zeno@bafh.org> 1.11-3
- minor fixes
* Sun Nov 24 2019 zeno <zeno@bafh.org> 1.11-2
- disable generation of debug package
* Wed Nov 20 2019 zeno <zeno@bafh.org> 1.11-1
- bump version to 1.11
* Fri Aug 09 2019 zeno <zeno@bafh.org> 1.10-1
- bump version to 1.10
* Fri Jun 14 2019 zeno <zeno@bafh.org> 1.9-1
- bump version to 1.9
* Thu May 02 2019 zeno <zeno@bafh.org> 1.8-3
- use version variable in source
* Sat Apr 27 2019 zeno <zeno@bafh.org> 1.8-2
- add adb as a requirement
* Wed Apr 24 2019 zeno <zeno@bafh.org> 1.8-1
- Initial packaging
