Summary:	xosd
Name:		xosd
Version:	0.7.0
Release:	0
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
#URL:		-
BuildRequires:	XFree86-devel
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

#%description -l pl

%prep
%setup  -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6/{lib,include,lib/xmms/General,man/man3}

install -s libxosd.so $RPM_BUILD_ROOT/usr/X11R6/lib
install -s libxmms_osd.so $RPM_BUILD_ROOT/usr/X11R6/lib/xmms/General
install xosd.h $RPM_BUILD_ROOT/usr/X11R6/include
install xosd.3 $RPM_BUILD_ROOT/usr/X11R6/man/man3

gzip -9nf ChangeLog AUTHORS

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/libxosd.so
%attr(755,root,root) /usr/X11R6/lib/xmms/General/libxmms_osd.so
/usr/X11R6/include/xosd.h
/usr/X11R6/man/man3/xosd.3.gz
