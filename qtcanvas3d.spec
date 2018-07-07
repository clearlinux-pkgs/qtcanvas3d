#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtcanvas3d
Version  : 5.11.1
Release  : 7
URL      : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtcanvas3d-everywhere-src-5.11.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtcanvas3d-everywhere-src-5.11.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtcanvas3d-lib
Requires: qtcanvas3d-license
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5OpenGLExtensions)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras

%description
3D Models and textures used in the example courtesy of http://nobiax.deviantart.com/

%package lib
Summary: lib components for the qtcanvas3d package.
Group: Libraries
Requires: qtcanvas3d-license

%description lib
lib components for the qtcanvas3d package.


%package license
Summary: license components for the qtcanvas3d package.
Group: Default

%description license
license components for the qtcanvas3d package.


%prep
%setup -q -n qtcanvas3d-everywhere-src-5.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1530975789
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qtcanvas3d
cp LICENSE.LGPLv3 %{buildroot}/usr/share/doc/qtcanvas3d/LICENSE.LGPLv3
cp LICENSE.LGPL3 %{buildroot}/usr/share/doc/qtcanvas3d/LICENSE.LGPL3
cp LICENSE.GPLv3 %{buildroot}/usr/share/doc/qtcanvas3d/LICENSE.GPLv3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/doc/qtcanvas3d/LICENSE.GPL3-EXCEPT
cp LICENSE.GPL2 %{buildroot}/usr/share/doc/qtcanvas3d/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/doc/qtcanvas3d/LICENSE.GPL3
cp LICENSE.GPLv2 %{buildroot}/usr/share/doc/qtcanvas3d/LICENSE.GPLv2
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/QtCanvas3D/libqtcanvas3d.so
/usr/lib64/qt5/qml/QtCanvas3D/plugins.qmltypes
/usr/lib64/qt5/qml/QtCanvas3D/qmldir

%files license
%defattr(-,root,root,-)
/usr/share/doc/qtcanvas3d/LICENSE.GPL2
/usr/share/doc/qtcanvas3d/LICENSE.GPL3
/usr/share/doc/qtcanvas3d/LICENSE.GPL3-EXCEPT
/usr/share/doc/qtcanvas3d/LICENSE.GPLv2
/usr/share/doc/qtcanvas3d/LICENSE.GPLv3
/usr/share/doc/qtcanvas3d/LICENSE.LGPL3
/usr/share/doc/qtcanvas3d/LICENSE.LGPLv3
