Summary: Opentracker. An open bittorrent tracker.
Name: opentracker
Version: 15092020~git6411f15
Release: 1%{?dist}.edf

# This program is licensed under a Beerware license and some parts
# originate from project libowfat, which is licensed under GPL-2.
License: Beerware and GPL-2

Group: Applications/System
URL: https://erdgeist.org/gitweb/opentracker
Source: %{name}-%{version}.tar.gz
BuildRequires: libowfat-devel zlib-devel
Requires: glibc libowfat zlib

%description
This package contains an open and free bittorrent tracker project.
It aims for minimal resource usage and is intended to run at your
wlan router. Currently it is deployed as an open and free tracker
instance.

%prep
%setup -q

%build
for feature in WANT_SYNC_LIVE WANT_SYSLOGS WANT_RESTRICT_STATS WANT_COMPRESSION_GZIP
do
  sed -i "s/^#\(.*$$feature\)/\1/" Makefile
done
sed -i "s#LIBOWFAT_HEADERS=\$(PREFIX)/libowfat#LIBOWFAT_HEADERS=/usr/include/libowfat#g" Makefile
sed -i "s#LIBOWFAT_LIBRARY=\$(PREFIX)/libowfat#LIBOWFAT_LIBRARY=/usr/lib64#g" Makefile
make

%install
install -d %{buildroot}/usr/bin
install -d %{buildroot}/usr/share/doc/opentracker
install -d %{buildroot}/usr/share/opentracker
install -m 755 opentracker %{buildroot}/usr/bin
install -m 755 opentracker.debug %{buildroot}/usr/bin
install -m 644 opentracker.conf.sample %{buildroot}/usr/share/doc/opentracker
install -m 755 sync_daemon.pl %{buildroot}/usr/share/opentracker

%files
%defattr(-, root, root)
#%dir /usr/bin
#%dir /usr/share/doc/opentracker
#%dir /usr/share/opentracker
/usr/bin/opentracker
/usr/bin/opentracker.debug
/usr/share/doc/opentracker/opentracker.conf.sample
/usr/share/opentracker/sync_daemon.pl


%changelog
* Wed Sep 16 2020 Pierre Trespeuch <pierre-externe.trespeuch@edf.fr> 15092020~git6411f15-1el8.edf
- Initial RPM release
