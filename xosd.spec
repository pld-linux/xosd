#
# Conditional build:
%bcond_without	xmms	# without XMMS plugin
#
Summary:	On Screen Display (like in TV) for X11
Summary(es):	Subtítulos (como en la tele) para X11
Summary(pl):	Wy¶wietlanie napisów na ekranie podobnie jak w telewizorach (OSD)
Name:		xosd
Version:	2.2.12
Release:	5
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.ignavus.net/%{name}-%{version}.tar.bz2
# Source0-md5:	756d714cec908e4d4c956ff0e7dcd4c4
Patch0:		%{name}-am18.patch
Patch1:		%{name}-link.patch
URL:		http://www.ignavus.net/software.html
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
%if %{with xmms}
BuildRequires:	gdk-pixbuf-devel >= 0.22.0
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.7
%endif
Obsoletes:	libxosd2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XOSD allows On Screen Displaying on your monitor under X11. It could
show current volume while changing it, or information about new mail
arrival. It has plugin for XMMS attached as an example what it can do.

%description -l es
XOSD permite mostrar subtítulos u otros mensajes en el monitor bajo
X11. Podría ser usado para mostrar el volumen del sonido cuando éste
sea cambiado, o bien una información sobre correo electrónico recién
llegado. Hay un plugin para XMMS que puede servir como ejemplo de lo
que se puede hacer.

%description -l pl
XOSD s³u¿y do wy¶wietlania na monitorze napisów w sposób podobny do
tego jak to siê dzieje we wspó³czesnych telewizorach (OSD). Mo¿e on
pokazywaæ aktualn± g³o¶no¶æ podczas jej zmieniania, albo informacje o
nowej poczcie. Do programu zosta³a do³±czona wtyczka dla XMMS-a
pokazuj±ca, co tak naprawdê potrafi XOSD.

%package devel
Summary:	Header files and documentation for developers of XOSD
Summary(es):	Ficheros de cabecera y documentación de programadores para XOSD
Summary(pl):	Pliki nag³ówkowe oraz dokumentcja dla programistów XOSD
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXinerama-devel
Obsoletes:	libxosd2-devel

%description devel
Files allowing development of xosd-based applications.

%description devel -l es
Ficheros que permiten el desarrollo de aplicaciones basadas en xosd.

%description devel -l pl
Pliki pozwalaj±ce tworzyæ programy w oparciu o xosd.

%package static
Summary:	Static libraries for XOSD
Summary(es):	Bibliotecas estáticas para XOSD
Summary(pl):	Statyczne biblioteki dla XOSD
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static libraries for XOSD.

%description static -l es
Bibliotecas estáticas para XOSD.

%description static -l pl
Statyczne biblioteki dla XOSD.

%package -n xmms-general-xosd
Summary:	Plugin for XMMS that allows On Screen Displaying (OSD)
Summary(es):	Plugin para XMMS que permite mostrar informaciones en la pantalla (OSD)
Summary(pl):	Wtyczka dla XMMS-a, która umo¿liwa wy¶wietlanie informacji na ekranie (OSD)
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	xmms >= 1.2.7

%description -n xmms-general-xosd
Plugin for XMMS enabling On Screen Display (OSD) showing names of
played files, volume, etc.

%description -n xmms-general-xosd -l es
Plugin para XMMS que habilita mostrar sobre la pantalla los nombres de
los ficheros reproducidos, el volumen, etc.

%description -n xmms-general-xosd -l pl
Wtyczka dla XMMS-a pokazuj±ca na ekranie (OSD) aktualne informacje o
odgrywanej piosence, g³o¶no¶ci, itd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{!?with_xmms:echo 'AC_DEFUN([AM_PATH_XMMS],[])' >> acinclude.m4}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_xmms:--with-plugindir=%{xmms_general_plugindir}} \
	%{!?with_xmms:--disable-new-plugin}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{xmms_general_plugindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -f $RPM_BUILD_ROOT%{xmms_general_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS README
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

%if %{with xmms}
%files -n xmms-general-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{xmms_general_plugindir}/libxmms_osd*.so*
%dir %{_datadir}/xosd
%{_datadir}/xosd/*.png
%endif
