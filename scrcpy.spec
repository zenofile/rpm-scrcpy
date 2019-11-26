Name:           scrcpy
Version:        1.11
Release:        4%{?dist}
Summary:        Display and control your Android device

License:        ASL 2.0
URL:            https://github.com/Genymobile/%{name}

Source0:        https://github.com/Genymobile/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/Genymobile/%{name}/releases/download/v%{version}/%{name}-server-v%{version}

%global         debug_package %{nil}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)

Requires:       adb

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%prep
%autosetup -v

%build
%meson -Db_lto=true -Dprebuilt_server='%{S:1}'
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md DEVELOP.md FAQ.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Nov 26 2019 zeno <zeno@bafh.org> 1.11-4
- minor fixes
* Fri Nov 25 2019 zeno <zeno@bafh.org> 1.11-3
- minor fixes
* Fri Nov 24 2019 zeno <zeno@bafh.org> 1.11-2
- disable generation of debug package
* Fri Nov 20 2019 zeno <zeno@bafh.org> 1.11-1
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
