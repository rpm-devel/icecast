
Name:		icecast
Version:	2.1.0
Release:	%dist
Summary:	Xiph Streaming media server that supports multiple audio formats.

Group:		Applications/Multimedia
License:	GPL
URL:		http://www.icecast.org/
Vendor:		Xiph.org Foundation <team@icecast.org>
Source:     http://www.icecast.org/files/%{name}-%{version}.tar.gz

#BuildArch:      %BuildArch
Requires:       libvorbis >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
Requires:       libogg >= 1.0
BuildRequires:	libogg-devel >= 1.0
Requires:       curl >= 7.10.0
BuildRequires:	curl-devel >= 7.10.0
Requires:       libxml2
BuildRequires:	libxml2-devel
Requires:       libxslt
BuildRequires:	libxslt-devel

%description
Icecast is a streaming media server which currently supports Ogg Vorbis
and MP3 audio streams. It can be used to create an Internet radio
station or a privately running jukebox and many things in between.
It is very versatile in that new formats can be added relatively
easily and supports open standards for commuincation and interaction.

%prep
rm -rf %_builddir/%{name}-%{version}
git clone -q https://github.com/karlheyes/icecast-kh.git %_builddir/%{name}-%{version}
cd %_builddir && tar cfz $HOME/rpmbuild/%{name}/%{name}-%{version}.tar.gz %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS TODO
%doc doc/*.html
%doc doc/*.jpg
%doc doc/*.css
%config(noreplace) /etc/%{name}.xml
%{_bindir}/icecast
%{_prefix}/share/icecast/*

%changelog
* Fri May 31 2019 CasjaysDev <rpm-admin@rpm-devel.casjaysdev.pro> - 2.1.0
- Initial Build for fedora

