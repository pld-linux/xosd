Summary:	On Screen Display (like in TV) for X11
Summary(pl):	Wy�wietlanie napis�w na ekranie podobnie jak w telewizorach (OSD)
Name:		xosd
Version:	0.7.0
Release:	0
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

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/{lib,include,lib/xmms/General,man/man3}

install -s libxosd.so $RPM_BUILD_ROOT%{_prefix}/lib
install -s libxmms_osd.so $RPM_BUILD_ROOT%{_prefix}/lib/xmms/General
install xosd.h $RPM_BUILD_ROOT%{_prefix}/include
install xosd.3 $RPM_BUILD_ROOT%{_prefix}/man/man3

gzip -9nf ChangeLog AUTHORS

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/lib/libxosd.so
%attr(755,root,root) %{_prefix}/lib/xmms/General/libxmms_osd.so
%{_prefix}/include/xosd.h
%{_prefix}/man/man3/xosd.3.gz
