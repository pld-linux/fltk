Summary:	Fast Light Tool Kit 
Summary(pl):	FLTK
Name:		fltk
Version:	1.0.8
Release:	1
License:	GPL
Group:		X11/Window Manager
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%name-%version-source.tar.bz2
Source1:	http://www.fltk.org/doc/%name.ps.gz
Source2:	http://www.fltk.org/doc/%name.pdf
URL:		http://www.fltk.org/
#Patch0:		
BuildRequires:	XFree86-devel >= 3.3.6
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description


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
CXXFLAGS="-O2 -mpentium -shared"
export CXXFLAGS
%configure \
	    --enable-shared \
	    --with-x

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

install %{SOURCE1} $RPM_BUILD_DIR/%name-%version/
install %{SOURCE2} $RPM_BUILD_DIR/%name-%version/


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/FL,%{_libdir}}
make libdir=$RPM_BUILD_ROOT%{_libdir} \
     includedir=$RPM_BUILD_ROOT%{_includedir} \
     bindir=$RPM_BUILD_ROOT%{_bindir} \
     install

cd $RPM_BUILD_ROOT%{_includedir}
    rm -f FL/*.h
    for file in FL/*.H; do \
    newfile="`basename $file H`h";\
    mv $file FL/$newfile
    done 

rm $RPM_BUILD_ROOT%{_libdir}/*.so
mv $RPM_BUILD_ROOT%{_libdir}/libfltk.so.1 \
    $RPM_BUILD_ROOT%{_libdir}/libfltk.so.%{version}

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

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
