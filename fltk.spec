Summary:	Fast Light Tool Kit 
Summary(pl):	FLTK
Name:		fltk
Version:	1.0.8
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%name-%version-source.tar.bz2
Source1:	http://www.fltk.org/doc/%name.ps.gz
Source2:	http://www.fltk.org/doc/%name.pdf
URL:		http://www.fltk.org/
#Patch0:	
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


%package static
Summary:	FLTK static library.
Summary(pl):	Biblioteka FLTK linkowana statycznie
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description static

%description -l pl static


%package devel
Summary:	FLTK development.
Summary(pl):	Narzêdzia programistyczne dla FLTK.
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description devel

%description -l pl devel

%prep
%setup -q

%build
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS CXXFLAGS
%configure \
	    --enable-shared \
	    --with-x

%{__make} depend
make

install %{SOURCE1} $RPM_BUILD_DIR/%name-%version/
install %{SOURCE2} $RPM_BUILD_DIR/%name-%version/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/FL,%{_libdir}}

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

cd $RPM_BUILD_ROOT%{_includedir}
rm -f FL/*.h
for file in FL/*.H; do
	newfile="`basename $file H`h"
	mv $file FL/$newfile
done 

rm $RPM_BUILD_ROOT%{_libdir}/*.so
mv $RPM_BUILD_ROOT%{_libdir}/libfltk.so.1 \
	$RPM_BUILD_ROOT%{_libdir}/libfltk.so.%{version}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.so.*.*.*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a

%files devel
%defattr(644,root,root,755)
%doc documentation/* fltk.pdf fltk.ps.gz
%attr(755,root,root) %{_bindir}/fluid
%attr(644,root,root) %{_includedir}/FL/*
