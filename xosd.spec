Summary:	On Screen Display (like in TV) for X11
Summary(pl):	Wy¶wietlanie napisów na ekranie podobnie jak w telewizorach (OSD)
Name:		xosd
Version:	2.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.ignavus.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-include.patch
URL:		http://www.ignavus.net/software.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XOSD allows On Screen Displaying on your monitor under X11. It could
show current volume while changing it, or information about new mail
arrival. It has plugin for XMMS attached as an example what it can do.

%description -l pl
XOSD s³u¿y do wy¶wietlania na monitorze napisów w sposób podobny
do tego jak to siê dzieje we wspó³czesnych telewizorach (OSD). Mo¿e on
pokazywaæ aktualn± g³o¶no¶æ podczas jej zmieniania, albo informacje o
nowej poczcie. Do programu zosta³a do³±czona wtyczka dla XMMS
pokazuj±ca, co tak naprawdê potrafi XOSD.

%package devel
Summary:	Header files and documentation for developers of XOSD
Summary(pl):	Pliki nag³ówkowe oraz dokumentcja dla programistów XOSD
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Files allowing development of xosd-based applications.

%description devel -l pl
Pliki pozwalaj±ce tworzyæ programy w oparciu o xosd.

%package static
Summary:	Static libraries for XOSD
Summary(pl):	Statyczne biblioteki dla XOSD
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description static
Static libraries for XOSD.

%description static -l pl
Statyczne biblioteki dla XOSD.

%package -n xmms-general-xosd
Summary:	Plugin for XMMS that allows On Screen Displaying (OSD)
Summary(pl):	Wtyczka dla XMMS, która umo¿liwa wy¶wietlanie informacji na ekranie (OSD)
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}
Requires:	xmms

%description -n xmms-general-xosd
Plugin for XMMS enabling On Screen Display (OSD) showing names of
played files, volume, etc.

%description -n xmms-general-xosd -l pl
Wtyczka dla XMMS pokazuj±ca na ekranie (OSD) aktualne informacje o
odgrywanej piosence, g³o¶no¶ci, itd.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
autoconf
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/xmms/General,%{_includedir},%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/osd_cat
%attr(755,root,root) %{_libdir}/libxosd.so.*.*.*
%{_mandir}/man1/*.1*

%files -n xmms-general-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/General/libxmms_osd.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xosd-config
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/xmms/General/libxmms_osd.la
%{_includedir}/*.h
%{_aclocaldir}/libxosd.m4
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libxosd.a
