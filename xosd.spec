Summary:	On Screen Display (like in TV) for X11
Summary(pl):	Wy¶wietlanie napisów na ekranie podobnie jak w telewizorach (OSD)
Name:		xosd
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.ignavus.net/%{name}-%{version}.tar.gz
URL:		http://www.ignavus.net/software.html
BuildRequires:	XFree86-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XOSD allows On Screen Displaying on your monitor under X11. It could
show current volume while changing it, or information about new mail
arrival. It has plugin for XMMS attached as an example what it can do.

%description -l pl
XOSD s³u¿y do wy¶wietlania na Twoim monitorze napisów w sposób podobny
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

%package -n xmms-general-xosd
Summary:	Plugin for XMMS that allows On Screen Displaying (OSD)
Summary(pl):	Wtyczka dla XMMS, która umo¿liwa wy¶wietlanie informacji na ekranie (OSD)
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description -n xmms-general-xosd
Plugin for XMMS enabling On Screen Display (OSD) showing names of
played files, volume, etc.

%description -n xmms-general-xosd -l pl
Wtyczka dla XMMS pokazuj±ca na ekranie (OSD) aktualne informacje o
odgrywanej piosence, g³o¶no¶ci, itd.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/xmms/General,%{_includedir},%{_mandir}/man3}

install libxosd.so $RPM_BUILD_ROOT%{_libdir}
install libxmms_osd.so $RPM_BUILD_ROOT%{_libdir}/xmms/General
install xosd.h $RPM_BUILD_ROOT%{_includedir}
install xosd.3 $RPM_BUILD_ROOT%{_mandir}/man3

gzip -9nf ChangeLog AUTHORS

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxosd.so

%files -n xmms-general-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/General/libxmms_osd.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/xosd.h
%{_mandir}/man3/xosd.3*
