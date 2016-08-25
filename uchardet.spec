Summary:	Encoding detector library
Summary(pl.UTF-8):	Biblioteka wykrywająca kodowanie
Name:		uchardet
Version:	0.0.6
Release:	1
License:	MPL v1.1
Group:		Libraries
Source0:	https://www.freedesktop.org/software/uchardet/releases/%{name}-%{version}.tar.xz
# Source0-md5:	03425c0bbe5faaf399e15e947d3e03c7
URL:		https://www.freedesktop.org/wiki/Software/uchardet/
BuildRequires:	cmake >= 2.8.5
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uchardet is an encoding detector library, which takes a sequence of
bytes in an unknown character encoding without any additional
information, and attempts to determine the encoding of the text.
Returned encoding names are iconv-compatible.

uchardet started as a C language binding of the original C++
implementation of the universal charset detection library by Mozilla.
It can now detect more charsets, and more reliably than the original
implementation.

%description -l pl.UTF-8
uchardet to biblioteka wykrywająca kodowanie znaków - przyjmująca
sekwencję bajtów o nieznanym kodowaniu bez dodatkowych informacji i
próbująca określić kodowanie tekstu. Zwracane nazwy kodowań są zgodne
z biblioteką iconv.

Biblioteka uchardet początkowo była wiązaniem C do oryginalnej
implementacji wykrywania znaków w C++, pochodzącej z projektu Mozilla.
Teraz może wykryć więcej zestawów znaków i jest bardziej wiarygodna od
oryginalnej implementacji.

%package devel
Summary:	Header file for uchardet library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki uchardet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header file for uchardet library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki uchardet.

%package static
Summary:	Static uchardet library
Summary(pl.UTF-8):	Statyczna biblioteka uchardet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static uchardet library.

%description static -l pl.UTF-8
Statyczna biblioteka uchardet.

%prep
%setup -q

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/uchardet
%attr(755,root,root) %{_libdir}/libuchardet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libuchardet.so.0
%{_mandir}/man1/uchardet.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libuchardet.so
%{_includedir}/uchardet
%{_pkgconfigdir}/uchardet.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libuchardet.a
