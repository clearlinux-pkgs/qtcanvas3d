#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtcanvas3d
Version  : 5.12.5
Release  : 19
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.5/submodules/qtcanvas3d-everywhere-src-5.12.5.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.5/submodules/qtcanvas3d-everywhere-src-5.12.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtcanvas3d-lib = %{version}-%{release}
Requires: qtcanvas3d-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5OpenGLExtensions)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : qtbase-staticdev

%description
3D Models and textures used in the example courtesy of http://nobiax.deviantart.com/

%package lib
Summary: lib components for the qtcanvas3d package.
Group: Libraries
Requires: qtcanvas3d-license = %{version}-%{release}

%description lib
lib components for the qtcanvas3d package.


%package license
Summary: license components for the qtcanvas3d package.
Group: Default

%description license
license components for the qtcanvas3d package.


%prep
%setup -q -n qtcanvas3d-everywhere-src-5.12.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1568396137
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtcanvas3d
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtcanvas3d/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtcanvas3d/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtcanvas3d/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtcanvas3d/LICENSE.LGPL3
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/QtCanvas3D/libqtcanvas3d.so
/usr/lib64/qt5/qml/QtCanvas3D/plugins.qmltypes
/usr/lib64/qt5/qml/QtCanvas3D/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtcanvas3d/LICENSE.GPL2
/usr/share/package-licenses/qtcanvas3d/LICENSE.GPL3
/usr/share/package-licenses/qtcanvas3d/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtcanvas3d/LICENSE.LGPL3
