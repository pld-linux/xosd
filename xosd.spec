Summary:	On Screen Display (like in TV) for X11
Summary(pl):	Wy�wietlanie napis�w na ekranie podobnie jak w telewizorach (OSD)
Name:		xosd
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt):	X11/Aplica��es
Group(pt_BR):	X11/Aplica��es
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
XOSD s�u�y do wy�wietlania na Twoim monitorze napis�w w spos�b podobny
do tego jak to si� dzieje we wsp�czesnych telewizorach (OSD). Mo�e on
pokazywa� aktualn� g�o�no�� podczas jej zmieniania, albo informacje o
nowej poczcie. Do programu zosta�a do��czona wtyczka dla XMMS
pokazuj�ca, co tak naprawd� potrafi XOSD.

%package devel
Summary:	Header files and documentation for developers of XOSD
Summary(pl):	Pliki nag��wkowe oraz dokumentcja dla programist�w XOSD
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name} = %{version}

%description devel
Files allowing development of xosd-based applications.

%description devel -l pl
Pliki pozwalaj�ce tworzy� programy w oparciu o xosd.

%package -n xmms-general-xosd
Summary:	Plugin for XMMS that allows On Screen Displaying (OSD)
Summary(pl):	Wtyczka dla XMMS, kt�ra umo�liwa wy�wietlanie informacji na ekranie (OSD)
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description -n xmms-general-xosd
Plugin for XMMS enabling On Screen Display (OSD) showing names of
played files, volume, etc.

%description -n xmms-general-xosd -l pl
Wtyczka dla XMMS pokazuj�ca na ekranie (OSD) aktualne informacje o
odgrywanej piosence, g�o�no�ci, itd.

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
