Summary:	Fast Light Tool Kit 
Summary(pl):	FLTK - "lekki" X11 toolkit 
Name:		fltk
Version:	1.0.11
Release:	3
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%{name}-%{version}-source.tar.bz2
Source1:	http://www.fltk.org/doc/%{name}.ps.gz
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

%package devel
Summary:	FLTK development files
Summary(pl):	Narzêdzia programistyczne dla FLTK
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
FLTK development files.

%description -l pl devel
Narzêdzia programistyczne dla FLTK.

%package static
Summary:	FLTK static library.
Summary(pl):	Biblioteka FLTK linkowana statycznie
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
FLTK static library.

%description -l pl static
Biblioteka FLTK linkowana statycznie.

%prep
%setup -q

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

(cd fluid;%{__make} install)
(cd src;%{__make} install)

rm $RPM_BUILD_ROOT%{_libdir}/*.so
mv $RPM_BUILD_ROOT%{_libdir}/libfltk.so.1 \
	$RPM_BUILD_ROOT%{_libdir}/libfltk.so.%{version}
ln -sf libfltk.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libfltk.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
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
