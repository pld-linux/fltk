Summary:	Fast Light Tool Kit
Summary(pl):	FLTK - "lekki" X11 toolkit
Summary(pt_BR):	Interface gráfica em C++ para X, OpenGL e Windows
Name:		fltk
Version:	1.0.11
Release:	6
License:	LGPL with amendments (see COPYING)
Group:		X11/Libraries
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Source1:	http://www.fltk.org/doc/%{name}.ps.gz
Patch0:		%{name}-fluid-shared.patch
URL:		http://www.fltk.org/
BuildRequires:	XFree86-devel >= 3.3.6
BuildRequires:	gcc-c++
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libfltk1.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
Requires:	%{name} = %{version}
Obsoletes:	libfltk1.1-devel

%description devel
FLTK development files.

%description devel -l pl
Narzêdzia programistyczne dla FLTK.

%description devel -l pt_BR
Arquivos de inclusão para o FLTK.

%package static
Summary:	FLTK static library.
Summary(pl):	Biblioteka FLTK linkowana statycznie
Summary(pt_BR):	Bibliotecas estáticas para o FLTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
FLTK static library.

%description static -l pl
Biblioteka FLTK linkowana statycznie.

%description static -l pt_BR
Bibliotecas estáticas para o FLTK.

%prep
%setup -q
%patch -p1

install %{SOURCE1} .

%build
%configure2_13 \
	--libdir=$RPM_BUILD_ROOT%{_libdir} \
	--includedir=$RPM_BUILD_ROOT%{_includedir} \
	--bindir=$RPM_BUILD_ROOT%{_bindir} \
	--enable-shared \
	--with-x

%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/FL,%{_libdir},%{_mandir}/man1}

cd fluid
%{__make} install
cd ../src
%{__make} install
cd ..

rm -f $RPM_BUILD_ROOT%{_libdir}/*.so
mv -f $RPM_BUILD_ROOT%{_libdir}/libfltk.so.1 \
	$RPM_BUILD_ROOT%{_libdir}/libfltk.so.%{version}
ln -sf libfltk.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libfltk.so
mv -f documentation/fltk.man $RPM_BUILD_ROOT%{_mandir}/man1/fltk.1
mv -f documentation/fluid.man $RPM_BUILD_ROOT%{_mandir}/man1/fluid.1

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
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
