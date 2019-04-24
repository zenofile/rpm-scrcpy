Name:           scrcpy
Version:        1.8
Release:        1%{?dist}
Summary:        Display and control your Android device 
License:        ASL 2.0
URL:            https://github.com/Genymobile/scrcpy

Source0:        https://github.com/Genymobile/%{name}/archive/v%{version}.tar.gz
Source1:        https://github.com/Genymobile/scrcpy/releases/download/v1.8/scrcpy-server-v1.8.jar

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  java-1.8.0-openjdk-devel 
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)

%description
Display and control your Android device.

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

%changelog
* Wed Apr 24 2019 zeno <zeno@bafh.org> 1.8-1
- Initial packaging
