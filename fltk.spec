#
# Conditional build:
# _without_gl	- without OpenGL support
#
Summary:	Fast Light Tool Kit
Summary(pl):	FLTK - "lekki" X11 toolkit
Summary(pt_BR):	Interface gr�fica em C++ para X, OpenGL e Windows
Name:		fltk
Version:	1.1.3
Release:	1
License:	LGPL with amendments (see COPYING)
Group:		X11/Libraries
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Source1:	http://www.fltk.org/doc-1.1/%{name}.ps.gz
Patch0:		%{name}-link.patch
URL:		http://www.fltk.org/
%{!?_without_gl:BuildRequires: OpenGL-devel}
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	gcc-c++
%{!?_without_gl:Requires: OpenGL}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libfltk1.1

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r), and
Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally developed
by Mr. Bill Spitzak and is currently maintained by a small group of
developers across the world with a central repository in the US.

%description -l pl
Fast Light Tool Kit ("FLTK", wymawiane "faltik"), jest rozprowadzanym
na licencji LGPL narz�dziem do tworzenia graficznych interfejs�w
u�ytkownika w C++ dla X (UNIX(r)), OpenGL(r), i Microsoft(r)
Windows(r) NT 4.0, 95, oraz 98. Jego pierwotnym autorem jest pan Bill
Spitzak; obecnie pakiet jest rozwijany przez niewielk� grup�
deweloper�w z r�nych stron �wiata (centralne repozytorium znajduje
si� w USA).

%description -l pt_BR
A Fast Light Tool Kit ("FLTK", pronuncia-se "fulltick") � uma
ferramenta e interface gr�fica feita em C++ para desenvolver
aplicativos para o X, OpenGL e Windows.

%package devel
Summary:	FLTK development files
Summary(pl):	Narz�dzia programistyczne dla FLTK
Summary(pt_BR):	Arquivos de inclus�o para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libfltk1.1-devel

%description devel
FLTK development files.

%description devel -l pl
Narz�dzia programistyczne dla FLTK.

%description devel -l pt_BR
Arquivos de inclus�o para o FLTK.

%package static
Summary:	FLTK static library
Summary(pl):	Biblioteka FLTK linkowana statycznie
Summary(pt_BR):	Bibliotecas est�ticas para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
FLTK static library.

%description static -l pl
Biblioteka FLTK linkowana statycznie.

%description static -l pt_BR
Bibliotecas est�ticas para o FLTK.

%prep
%setup -q
%patch -p1

install %{SOURCE1} .

%build
CPPFLAGS="-I/usr/X11R6/include"
%configure \
	--enable-shared \
	--with-x \
	%{?_without_gl:--disable-gl}

%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/FL,%{_libdir},%{_mandir}/man{1,3}}

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc documentation/*.{html,gif,jpg} fltk.ps.gz
%attr(755,root,root) %{_bindir}/fltk-config
%attr(755,root,root) %{_bindir}/fluid
%attr(755,root,root) %{_libdir}/libfltk.so
%{_includedir}/FL
%{_mandir}/man[13]/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
