Summary:	Fast Light Tool Kit
Summary(pl):	FLTK - "lekki" X11 toolkit
Name:		fltk
Version:	1.0.11
Release:	5
License:	LGPL with amendments (see COPYING)
Group:		X11/Libraries
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Source1:	http://www.fltk.org/doc/%{name}.ps.gz
Patch0:		%{name}-fluid-shared.patch
URL:		http://www.fltk.org/
BuildRequires:	XFree86-devel >= 3.3.6
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r), and
Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally developed
by Mr. Bill Spitzak and is currently maintained by a small group of
developers across the world with a central repository in the US.

%description -l pl
Fast Light Tool Kit ("FLTK", wymawiane "faltik"), jest rozprowadzanym
na licencji LGPL narz�dziem do tworzenia graficznych interfejs�w
u�ytkownika w C++ dla X (UNIX(r)), OpenGL(r), i Microsoft(r) Windows(r) 
NT 4.0, 95, oraz 98. Jego pierwotnym autorem jest pan Bill Spitzak; obecnie 
pakiet jest rozwijany przez niewielk� grup� deweloper�w z r�nych stron 
�wiata (centralne repozytorium znajduje si� w USA).

%package devel
Summary:	FLTK development files
Summary(pl):	Narz�dzia programistyczne dla FLTK
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
FLTK development files.

%description devel -l pl
Narz�dzia programistyczne dla FLTK.

%package static
Summary:	FLTK static library.
Summary(pl):	Biblioteka FLTK linkowana statycznie
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
FLTK static library.

%description static -l pl
Biblioteka FLTK linkowana statycznie.

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/FL,%{_libdir}}

cd fluid
%{__make} install
cd ../src
%{__make} install
cd ..

rm -f $RPM_BUILD_ROOT%{_libdir}/*.so
mv -f $RPM_BUILD_ROOT%{_libdir}/libfltk.so.1 \
	$RPM_BUILD_ROOT%{_libdir}/libfltk.so.%{version}
ln -sf libfltk.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libfltk.so

# note: COPYING contains amendments to LGPL, so don't remove!
gzip -9nf CHANGES COPYING README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc [CR]*.gz
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc documentation/* fltk.ps.gz
%attr(75,root,root) %{_libdir}/libfltk.so
%attr(755,root,root) %{_bindir}/fluid
%{_includedir}/FL

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
