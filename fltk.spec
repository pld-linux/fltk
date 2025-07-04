#
# Conditional build:
%bcond_without	opengl	# OpenGL libraries
%bcond_without	xft	# Xft support
#
Summary:	Fast Light Tool Kit
Summary(pl.UTF-8):	FLTK - "lekki" X11 toolkit
Summary(pt_BR.UTF-8):	Interface gráfica em C++ para X, OpenGL e Windows
Name:		fltk
Version:	1.3.11
Release:	1
License:	LGPL v2 with amendments (see COPYING)
Group:		X11/Libraries
#Source0Download: https://www.fltk.org/software.php
Source0:	https://github.com/fltk/fltk/releases/download/release-%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	0e79fa6c4caad1d219b381330f2a0ea2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-as-needed.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-mime.patch
Patch5:		%{name}-docdir.patch
URL:		http://www.fltk.org/
%{?with_opengl:BuildRequires:	OpenGL-GLU-devel}
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	cairo-devel
BuildRequires:	doxygen
%{?with_xft:BuildRequires:	fontconfig-devel}
BuildRequires:	groff
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.315
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
%{?with_xft:BuildRequires:	xorg-lib-libXft-devel}
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-util-makedepend
Obsoletes:	libfltk1.1 < 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't propagate strip-flags to fltk-config.
%define		filterout_ld	(-Wl,)?-[sS] (-Wl,)?--strip.*

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r), and
Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally developed
by Mr. Bill Spitzak and is currently maintained by a small group of
developers across the world with a central repository in the US.

%description -l pl.UTF-8
Fast Light Tool Kit ("FLTK", wymawiane "fultik"), jest rozprowadzanym
na licencji LGPL narzędziem do tworzenia graficznych interfejsów
użytkownika w C++ dla X (UNIX(r)), OpenGL(r), i Microsoft(r)
Windows(r) NT 4.0, 95, oraz 98. Jego pierwotnym autorem jest pan Bill
Spitzak; obecnie pakiet jest rozwijany przez niewielką grupę
deweloperów z różnych stron świata (centralne repozytorium znajduje
się w USA).

%description -l pt_BR.UTF-8
A Fast Light Tool Kit ("FLTK", pronuncia-se "fulltick") é uma
ferramenta e interface gráfica feita em C++ para desenvolver
aplicativos para o X, OpenGL e Windows.

%package devel
Summary:	FLTK development files
Summary(pl.UTF-8):	Narzędzia programistyczne dla FLTK
Summary(pt_BR.UTF-8):	Arquivos de inclusão para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libstdc++-devel
%{?with_xft:Requires:	xorg-lib-libXft-devel}
Requires:	xorg-lib-libXinerama-devel
Obsoletes:	libfltk1.1-devel < 1.2

%description devel
FLTK development files.

%description devel -l pl.UTF-8
Narzędzia programistyczne dla FLTK.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para o FLTK.

%package static
Summary:	FLTK static library
Summary(pl.UTF-8):	Biblioteka FLTK konsolidowana statycznie
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FLTK static library.

%description static -l pl.UTF-8
Biblioteka FLTK konsolidowana statycznie.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para o FLTK.

%package cairo
Summary:	FLTK Cairo library
Summary(pl.UTF-8):	Biblioteka FLTK Cairo
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description cairo
FLTK Cairo library.

%description cairo -l pl.UTF-8
Biblioteka FLTK Cairo.

%package cairo-devel
Summary:	Header files for FLTK Cairo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FLTK Cairo
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-cairo = %{version}-%{release}

%description cairo-devel
Header files for FLTK Cairo library.

%description cairo-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FLTK Cairo.

%package cairo-static
Summary:	FLTK Cairo static library
Summary(pl.UTF-8):	Statyczna biblioteka FLTK Cairo
Group:		X11/Development/Libraries
Requires:	%{name}-cairo-devel = %{version}-%{release}

%description cairo-static
FLTK Cairo static library.

%description cairo-static -l pl.UTF-8
Statyczna biblioteka FLTK Cairo.

%package gl
Summary:	FLTK GL library
Summary(pl.UTF-8):	Biblioteka FLTK GL
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL

%description gl
FLTK GL library.

%description gl -l pl.UTF-8
Biblioteka FLTK GL.

%package gl-devel
Summary:	Header files for FLTK GL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FLTK GL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gl = %{version}-%{release}

%description gl-devel
Header files for FLTK GL library.

%description gl-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FLTK GL.

%package gl-static
Summary:	FLTK GL static library
Summary(pl.UTF-8):	Statyczna biblioteka FLTK GL
Group:		X11/Development/Libraries
Requires:	%{name}-gl-devel = %{version}-%{release}
Requires:	%{name}-static = %{version}-%{release}

%description gl-static
FLTK GL static library.

%description gl-static -l pl.UTF-8
Statyczna biblioteka FLTK GL.

%package apidocs
Summary:	API documentation for FLTK library
Summary(pl.UTF-8):	Dokumentacja API biblioteki FLTK
Group:		Documentation

%description apidocs
API documentation for FLTK library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki FLTK.

%package fluid
Summary:	FLTK GUI Designer
Summary(pl.UTF-8):	Narzędzie FLTK do projektowania GUI
Group:		X11/Development/Tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-cairo = %{version}-%{release}
Suggests:	%{name}-apidocs = %{version}-%{release}

%description fluid
FLTK GUI Designer.

%description fluid -l pl.UTF-8
Narzędzie FLTK do projektowania GUI.

%package games
Summary:	FLTK Games
Summary(pl.UTF-8):	Gry FLTK
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description games
FLTK games: Block Attack!, Checkers, or Sudoku on your computer.

%description games -l pl.UTF-8
Gry FLTK: Atak Klocków!, Warcaby, Sudoku.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P5 -p1

%build
# gold doesn't understand -l:path/to/library.so
if [ -x /usr/bin/ld.bfd ]; then
	install -d ld-dir
	ln -sf /usr/bin/ld.bfd ld-dir/ld
	export PATH=$(pwd)/ld-dir:$PATH
fi
%{__autoconf}
%configure \
	--enable-cairo \
	--enable-largefile \
	--enable-shared \
	--enable-threads \
	--enable-xinerama \
	--with-x \
	--with-optim="%{rpmcxxflags}" \
	%{!?with_opengl:--disable-gl} \
	%{?with_xft:--enable-xft}

%{__make}

%{__make} -C documentation html

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-desktop \
	DESTDIR=$RPM_BUILD_ROOT

# less generic games' names
for f in blocks checkers sudoku ; do
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{,fltk-}${f}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man6/{,fltk-}${f}.6
done

# we package mans in groff format
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/cat?

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   cairo -p /sbin/ldconfig
%postun cairo -p /sbin/ldconfig

%post   gl -p /sbin/ldconfig
%postun gl -p /sbin/ldconfig

%post	fluid
%update_icon_cache hicolor
%update_desktop_database
%update_mime_database

%postun	fluid
%update_icon_cache hicolor
%update_desktop_database
%update_mime_database

%post	games
%update_icon_cache hicolor

%postun	games
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
# note: COPYING contains amendments to LGPL, so don't remove!
%doc ANNOUNCEMENT CHANGES COPYING CREDITS README
%attr(755,root,root) %{_libdir}/libfltk.so.*.*
%attr(755,root,root) %{_libdir}/libfltk_forms.so.*.*
%attr(755,root,root) %{_libdir}/libfltk_images.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fltk-config
%attr(755,root,root) %{_libdir}/libfltk.so
%attr(755,root,root) %{_libdir}/libfltk_forms.so
%attr(755,root,root) %{_libdir}/libfltk_images.so
%{_includedir}/FL
%exclude %{_includedir}/FL/Fl_Cairo*.H
%exclude %{_includedir}/FL/Fl_Gl_Window.H
%exclude %{_includedir}/FL/gl*
%{_mandir}/man1/fltk-config.1*
%{_mandir}/man3/fltk.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfltk.a
%{_libdir}/libfltk_forms.a
%{_libdir}/libfltk_images.a

%files cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfltk_cairo.so.*.*

%files cairo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfltk_cairo.so
%{_includedir}/FL/Fl_Cairo*.H

%files cairo-static
%defattr(644,root,root,755)
%{_libdir}/libfltk_cairo.a

%if %{with opengl}
%files gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfltk_gl.so.*.*

%files gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfltk_gl.so
%{_includedir}/FL/Fl_Gl_Window.H
%{_includedir}/FL/gl*

%files gl-static
%defattr(644,root,root,755)
%{_libdir}/libfltk_gl.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc documentation/html/*.{html,jpg,png}

%files fluid
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fluid
%{_iconsdir}/hicolor/*x*/apps/fluid.png
%{_desktopdir}/fluid.desktop
%{_datadir}/mime/packages/fluid.xml
%{_mandir}/man1/fluid.1*

%files games
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-blocks
%attr(755,root,root) %{_bindir}/%{name}-checkers
%attr(755,root,root) %{_bindir}/%{name}-sudoku
%{_iconsdir}/hicolor/*x*/apps/blocks.png
%{_iconsdir}/hicolor/*x*/apps/checkers.png
%{_iconsdir}/hicolor/*x*/apps/sudoku.png
%{_desktopdir}/blocks.desktop
%{_desktopdir}/checkers.desktop
%{_desktopdir}/sudoku.desktop
%{_mandir}/man6/%{name}-blocks.6*
%{_mandir}/man6/%{name}-checkers.6*
%{_mandir}/man6/%{name}-sudoku.6*
