Summary:	Fast Light Tool Kit 
Summary(pl):	FLTK
Name:		fltk
Version:	1.0.7
Release:	1
License:	GPL
Group:		WindowManagers
######		Unknown group!
Group(pl):	Menad¿erOkien
Source0:	ftp://ftp.easysw.com/pub/%{name}/%{version}/%name-%version-source.tar.bz2
Source1:	http://www.fltk.org/doc/%name.ps.gz
Source2:	http://www.fltk.org/doc/%name.pdf
URL:		http://www.fltk.org/
Patch0:		
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description


%description -l pl


%package	doc
Summary:	FLTK Documentation
Summary(pl):	FLTK Dokumentacja
Group:		Documentation
######		Unknown group!
Group(pl):	Dokumentacja

%description doc


%description -l pl doc


%package static
Summary:	FLTK static library.
Summary(pl):	Biblioteka FLTK linkowana statycznie
Group:		Libraries/Development
######		Unknown group!
Group(pl):	Biblioteki/Programowanie

%description static


%description -l pl static


%package devel
Summary:	FLTK development.
Summary(pl):	Narzêdzia programistyczne dla FLTK.
Group:		Libraries/Development
######		Unknown group!
Group(pl):	Biblioteki/Programowanie

%description devel


%description -l pl devel


%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
	    --enable-shared \
	    --with-x
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" depend
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

install %{SOURCE1} $RPM_BUILD_DIR/%name-%version/
install %{SOURCE2} $RPM_BUILD_DIR/%name-%version/


%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(644,root,root) %{_libdir}/*.so*

%files doc
%defattr(644,root,root,755)
%doc documentation/* fltk.pdf fltk.ps.gz

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/FL/*
