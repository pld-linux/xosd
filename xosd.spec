#
# Conditional build:
# _without_xmms		- without XMMS plugin
#
Summary:	On Screen Display (like in TV) for X11
Summary(pl):	Wy¶wietlanie napisów na ekranie podobnie jak w telewizorach (OSD)
Name:		xosd
Version:	2.2.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.ignavus.net/%{name}-%{version}.tar.gz
# Source0-md5:	b385858fb4ddeff0875fa5b4dc372e42
URL:		http://www.ignavus.net/software.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel >= 0.22.0
BuildRequires:	gtk+-devel
BuildRequires:	libtool
%{!?_without_xmms:BuildRequires:	rpmbuild(macros) >= 1.125}
%{!?_without_xmms:BuildRequires:	xmms-devel}
Obsoletes:	libxosd2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Obsoletes:	libxosd2-devel

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
Group:		X11/Applications/Sound
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

%build
rm -f missing
%{?_without_xmms:echo 'AC_DEFUN([AM_PATH_XMMS],[])' >> acinclude.m4}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?_without_xmms:--with-plugindir=%{xmms_general_plugindir}} \
	%{?_without_xmms:--disable-new-plugin}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{xmms_general_plugindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/osd_cat
%attr(755,root,root) %{_libdir}/libxosd.so.*.*.*
%{_mandir}/man1/osd_cat.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xosd-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h
%{_aclocaldir}/libxosd.m4
%{_mandir}/man3/*.3*
%{_mandir}/man1/xosd-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libxosd.a

%if 0%{!?_without_xmms:1}
%files -n xmms-general-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_general_plugindir}/libxmms_osd*.so*
%dir %{_datadir}/xosd
%{_datadir}/xosd/*.png
%endif
