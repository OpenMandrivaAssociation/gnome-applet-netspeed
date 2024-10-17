Name: gnome-applet-netspeed    
Version: 0.16
Release: %mkrel 1
Summary: GNOME applet that shows traffic on a network device

Group: Graphical desktop/GNOME
License: GPL   
URL: https://projects.gnome.org/netspeed/
Source0: http://launchpadlibrarian.net/49741506/netspeed_applet-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: pkgconfig, gettext, scrollkeeper, intltool
BuildRequires: perl-XML-Parser, gnome-doc-utils
BuildRequires: libgnomeui2-devel >= 2.8, libgtop2.0-devel
BuildRequires: gnome-panel-devel >= 2.8, libnotify-devel
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
Provides: netspeed_applet = %{version}-%{release}
Obsoletes: netspeed_applet <= 0.12.1

%description
netspeed is a little GNOME applet that shows the traffic on a
specified network device (for example eth0) in kbytes/s.

%prep
%setup -q -n netspeed_applet-%{version}

%build
%configure2_5x --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang netspeed_applet

%post
scrollkeeper-update -q -o %{_datadir}/omf/netspeed_applet || : 

%postun
scrollkeeper-update -q || :

%clean
rm -rf $RPM_BUILD_ROOT


%files -f netspeed_applet.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_datadir}/gnome/help/netspeed_applet/
%{_libexecdir}/netspeed_applet2
%{_libdir}/bonobo/servers/*
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/omf/netspeed_applet/
