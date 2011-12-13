# TODO: enable cairo support?
#
# Conditional build:
%bcond_without	opengl	# without OpenGL libraries
%bcond_without	xft	# without Xft support
#
Summary:	Fast Light Tool Kit
Summary(pl.UTF-8):	FLTK - "lekki" X11 toolkit
Summary(pt_BR.UTF-8):	Interface gráfica em C++ para X, OpenGL e Windows
Name:		fltk
Version:	1.3.0
Release:	1
License:	LGPL with amendments (see COPYING)
Group:		X11/Libraries
Source0:	http://ftp.easysw.com/pub/fltk/%{version}/%{name}-%{version}-source.tar.gz
# Source0-md5:	44d5d7ba06afdd36ea17da6b4b703ca3
Source1:	http://ftp.easysw.com/pub/fltk/%{version}/%{name}-%{version}-docs-html.tar.gz
# Source1-md5:	ee79155cffc211e1d70a3ad8d3f170ef
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-1.3.0-as-needed.patch
Patch2:		%{name}-link.patch
URL:		http://www.fltk.org/
%{?with_opengl:BuildRequires:	OpenGL-GLU-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	groff
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.315
BuildRequires:	xorg-lib-libXext-devel
%{?with_xft:BuildRequires:	xorg-lib-libXft-devel}
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-util-makedepend
Obsoletes:	libfltk1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
Obsoletes:	libfltk1.1-devel

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
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure \
	--enable-largefile \
	--enable-shared \
	--enable-threads \
	--enable-xinerama \
	--with-x \
	--with-optim="%{rpmcxxflags}" \
	%{!?with_opengl:--disable-gl} \
	%{?with_xft:--enable-xft}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install-desktop \
	DESTDIR=$RPM_BUILD_ROOT

# less generic games' names
for f in blocks checkers sudoku ; do
mv -f $RPM_BUILD_ROOT%{_bindir}/{,fltk-}${f}
mv -f $RPM_BUILD_ROOT%{_mandir}/man6/{,fltk-}${f}.6
done

# add link to documentation for fluid help; remove /usr/share/doc/fltk contents - it is installed during make install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
ln -sf %{name}-devel-%{version} $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# note: COPYING contains amendments to LGPL, so don't remove!
%doc CHANGES COPYING CREDITS README
%attr(755,root,root) %{_libdir}/libfltk.so.*.*
%attr(755,root,root) %{_libdir}/libfltk_forms.so.*.*
%attr(755,root,root) %{_libdir}/libfltk_images.so.*.*

%files devel
%defattr(644,root,root,755)
%doc fltk-%{version}/documentation/html/*.{html,jpg,png}
%doc %{_datadir}/doc/%{name}
%attr(755,root,root) %{_bindir}/fltk-config
%attr(755,root,root) %{_bindir}/fluid
%attr(755,root,root) %{_libdir}/libfltk.so
%attr(755,root,root) %{_libdir}/libfltk_forms.so
%attr(755,root,root) %{_libdir}/libfltk_images.so
%{_includedir}/FL
%exclude %{_includedir}/FL/Fl_Gl_Window.*
%exclude %{_includedir}/FL/gl*
%{_iconsdir}/*/*/*/fluid.png
%{_desktopdir}/fluid.desktop
# move to some KDE package?
#%{_datadir}/mimelnk/application/x-fluid.desktop
%{_mandir}/man1/fltk-config.1*
%{_mandir}/man1/fluid.1*
%{_mandir}/man3/fltk.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfltk.a
%{_libdir}/libfltk_forms.a
%{_libdir}/libfltk_images.a

%if %{with opengl}
%files gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfltk_gl.so.*.*

%files gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfltk_gl.so
%{_includedir}/FL/Fl_Gl_Window.*
%{_includedir}/FL/gl*

%files gl-static
%defattr(644,root,root,755)
%{_libdir}/libfltk_gl.a
%endif

%files games
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-blocks
%attr(755,root,root) %{_bindir}/%{name}-checkers
%attr(755,root,root) %{_bindir}/%{name}-sudoku
%{_iconsdir}/*/*/*/blocks.png
%{_iconsdir}/*/*/*/checkers.png
%{_iconsdir}/*/*/*/sudoku.png
%{_desktopdir}/blocks.desktop
%{_desktopdir}/checkers.desktop
%{_desktopdir}/sudoku.desktop
%{_mandir}/man6/%{name}-blocks.6*
%{_mandir}/man6/%{name}-checkers.6*
%{_mandir}/man6/%{name}-sudoku.6*
