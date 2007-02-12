#
# Conditional build:
# _without_gl	- without OpenGL support
#
Summary:	Fast Light Tool Kit
Summary(pl.UTF-8):   FLTK - "lekki" X11 toolkit
Summary(pt_BR.UTF-8):   Interface gráfica em C++ para X, OpenGL e Windows
Name:		fltk
Version:	1.1.0rc2
Release:	1
License:	LGPL with amendments (see COPYING)
Group:		X11/Libraries
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Source1:	http://www.fltk.org/doc/%{name}.ps.gz
Patch0:		%{name}-fluid-shared.patch
URL:		http://www.fltk.org/
%{!?_without_gl:BuildRequires: OpenGL-devel}
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	gcc-c++
%{!?_without_gl:Requires: OpenGL}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libfltk1.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r), and
Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally developed
by Mr. Bill Spitzak and is currently maintained by a small group of
developers across the world with a central repository in the US.

%description -l pl.UTF-8
Fast Light Tool Kit ("FLTK", wymawiane "faltik"), jest rozprowadzanym
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
Summary(pl.UTF-8):   Narzędzia programistyczne dla FLTK
Summary(pt_BR.UTF-8):   Arquivos de inclusão para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libfltk1.1-devel

%description devel
FLTK development files.

%description devel -l pl.UTF-8
Narzędzia programistyczne dla FLTK.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para o FLTK.

%package static
Summary:	FLTK static library.
Summary(pl.UTF-8):   Biblioteka FLTK linkowana statycznie
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
FLTK static library.

%description static -l pl.UTF-8
Biblioteka FLTK linkowana statycznie.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para o FLTK.

%prep
%setup -q
#%patch -p1

install %{SOURCE1} .

%build
CPPFLAGS="-I/usr/X11R6/include"; export CPPFLAGS
%configure2_13 \
	--libdir=$RPM_BUILD_ROOT%{_libdir} \
	--includedir=$RPM_BUILD_ROOT%{_includedir} \
	--bindir=$RPM_BUILD_ROOT%{_bindir} \
	--enable-shared \
	--with-x \
	%{?_without_gl:--disable-gl}

%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/FL,%{_libdir},%{_mandir}/man1}

install fltk-config $RPM_BUILD_ROOT%{_bindir}/

cd fluid
%{__make} install
cd ../src
%{__make} install
cd ../FL
%{__make} install
cd ..

rm -f $RPM_BUILD_ROOT%{_libdir}/*.so
mv -f $RPM_BUILD_ROOT%{_libdir}/libfltk.so.1.1 \
	$RPM_BUILD_ROOT%{_libdir}/libfltk.so.%{version}
ln -sf libfltk.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libfltk.so
mv -f documentation/fltk.man $RPM_BUILD_ROOT%{_mandir}/man1/fltk.1
mv -f documentation/fluid.man $RPM_BUILD_ROOT%{_mandir}/man1/fluid.1
ln -s %{_includedir}/FL $RPM_BUILD_ROOT/%{_includedir}/Fl

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# note: COPYING contains amendments to LGPL, so don't remove!
%doc CHANGES COPYING README
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc documentation/* fltk.ps.gz
%attr(755,root,root) %{_libdir}/libfltk.so
%attr(755,root,root) %{_bindir}/fluid
%{_includedir}/FL
%{_includedir}/Fl
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
