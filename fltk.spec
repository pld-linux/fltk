#
# Conditional build:
%bcond_without	gl	# without OpenGL libraries
%bcond_without	xft	# without Xft support
#
Summary:	Fast Light Tool Kit
Summary(pl):	FLTK - "lekki" X11 toolkit
Summary(pt_BR):	Interface gráfica em C++ para X, OpenGL e Windows
Name:		fltk
Version:	1.1.4
Release:	1
License:	LGPL with amendments (see COPYING)
Group:		X11/Libraries
Source0:	ftp://ftp.easysw.com/pub/fltk/%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	06ce1d3def2df35525592746faccbf98
Source1:	http://www.fltk.org/doc-1.1/%{name}.ps.gz
# Source1-md5:	eb8f5a4a02d8ca2111ff007daea601b6
Patch0:		%{name}-link.patch
URL:		http://www.fltk.org/
%{?with_gl:BuildRequires:	OpenGL-devel}
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
%{?with_xft:BuildRequires:	xft-devel}
Obsoletes:	libfltk1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r), and
Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally developed
by Mr. Bill Spitzak and is currently maintained by a small group of
developers across the world with a central repository in the US.

%description -l pl
Fast Light Tool Kit ("FLTK", wymawiane "faltik"), jest rozprowadzanym
na licencji LGPL narzêdziem do tworzenia graficznych interfejsów
u¿ytkownika w C++ dla X (UNIX(r)), OpenGL(r), i Microsoft(r)
Windows(r) NT 4.0, 95, oraz 98. Jego pierwotnym autorem jest pan Bill
Spitzak; obecnie pakiet jest rozwijany przez niewielk± grupê
deweloperów z ró¿nych stron ¶wiata (centralne repozytorium znajduje
siê w USA).

%description -l pt_BR
A Fast Light Tool Kit ("FLTK", pronuncia-se "fulltick") é uma
ferramenta e interface gráfica feita em C++ para desenvolver
aplicativos para o X, OpenGL e Windows.

%package devel
Summary:	FLTK development files
Summary(pl):	Narzêdzia programistyczne dla FLTK
Summary(pt_BR):	Arquivos de inclusão para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Obsoletes:	libfltk1.1-devel

%description devel
FLTK development files.

%description devel -l pl
Narzêdzia programistyczne dla FLTK.

%description devel -l pt_BR
Arquivos de inclusão para o FLTK.

%package static
Summary:	FLTK static library
Summary(pl):	Biblioteka FLTK konsolidowana statycznie
Summary(pt_BR):	Bibliotecas estáticas para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FLTK static library.

%description static -l pl
Biblioteka FLTK konsolidowana statycznie.

%description static -l pt_BR
Bibliotecas estáticas para o FLTK.

%package gl
Summary:	FLTK GL library
Summary(pl):	Biblioteka FLTK GL
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL

%description gl
FLTK GL library.

%description gl -l pl
Biblioteka FLTK GL.

%package gl-devel
Summary:	Header files for FLTK GL library
Summary(pl):	Pliki nag³ówkowe biblioteki FLTK GL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gl = %{version}-%{release}

%description gl-devel
Header files for FLTK GL library.

%description gl-devel -l pl
Pliki nag³ówkowe biblioteki FLTK GL.

%package gl-static
Summary:	FLTK GL static library
Summary(pl):	Statyczna biblioteka FLTK GL
Group:		X11/Development/Libraries
Requires:	%{name}-gl-devel = %{version}-%{release}
Requires:	%{name}-static = %{version}-%{release}

%description gl-static
FLTK GL static library.

%description gl-static -l pl
Statyczna biblioteka FLTK GL.

%prep
%setup -q
%patch0 -p1

install %{SOURCE1} .

%build
CPPFLAGS="-I/usr/X11R6/include"
CXXFLAGS="%{rpmcflags} -I/usr/include/freetype2"
# no "-s" in LDFLAGS, they are propagated to fltk-config
# (together with -L/usr/X11R6/lib, so cannot be removed)
LDFLAGS=" "
%{__autoconf}
%configure \
	--enable-shared \
	--with-x \
	%{!?with_gl:--disable-gl} \
	%{?with_xft:--enable-xft}

%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/FL,%{_libdir},%{_mandir}/man{1,3}}

if [ "%{_lib}" != "lib" ] ; then
	ln -sf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_prefix}/lib
fi

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

if [ "%{_lib}" != "lib" ] ; then
	rm $RPM_BUILD_ROOT%{_prefix}/lib
fi

install documentation/fltk-config.man $RPM_BUILD_ROOT%{_mandir}/man1/fltk-config.1
install documentation/fluid.man $RPM_BUILD_ROOT%{_mandir}/man1/fluid.1
install documentation/fltk.man $RPM_BUILD_ROOT%{_mandir}/man3/fltk.3

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
%doc documentation/*.{html,gif,jpg} fltk.ps.gz
%attr(755,root,root) %{_bindir}/fltk-config
%attr(755,root,root) %{_bindir}/fluid
%attr(755,root,root) %{_libdir}/libfltk.so
%attr(755,root,root) %{_libdir}/libfltk_forms.so
%attr(755,root,root) %{_libdir}/libfltk_images.so
%{_includedir}/FL
%exclude %{_includedir}/FL/Fl_Gl_Window.*
%exclude %{_includedir}/FL/gl*
%{_mandir}/man[13]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfltk.a
%{_libdir}/libfltk_forms.a
%{_libdir}/libfltk_images.a

%if %{with gl}
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
