%define		gitrev	9d6b188fca185968af5c62438b44dcbd2eefc47a

Summary:	Movie player
Name:		mplayer2
Version:	2.0
Release:	0.%{gitrev}.1
License:	GPL
Group:		Applications/Multimedia
#Source0:	http://ftp.mplayer2.org/pub/archive/release/source/%{name}-%{version}.tar.xz
Source0:	http://git.mplayer2.org/mplayer2/snapshot/%{name}-%{gitrev}.tar.bz2
# Source0-md5:	160b1b10f92a773fda02eca5dbfc3d3c
Source1:	%{name}.desktop
URL:		http://www.mplayerhq.hu/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	docutils
BuildRequires:	faac-devel
BuildRequires:	faad2-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	giflib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libass-devel
BuildRequires:	libav-devel
BuildRequires:	libbluray-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdca-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libx264-devel
BuildRequires:	libxslt-progs
BuildRequires:	mpg123-libs-devel
BuildRequires:	ncurses-devel
BuildRequires:	opencore-amr-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRequires:	python3-modules
BuildRequires:	speex-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXv-devel
BuildRequires:	xorg-libXvMC-devel
BuildRequires:	xorg-libXxf86dga-devel
BuildRequires:	xorg-libXxf86vm-devel
BuildRequires:	xvidcore-devel
BuildRequires:	zlib-devel
Conflicts:	mplayer
Requires(post,postun):	desktop-file-utils
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
MPlayer is a movie player.

%prep
%setup -qn %{name}-%{gitrev}

echo %{version} > VERSION

cp -f etc/codecs.conf etc/codecs.win32.conf

%build
CC="%{__cc}"
export CC

./configure \
	--codecsdir=%{_libdir}/codecs		\
	--confdir=%{_sysconfdir}/mplayer	\
	--disable-caca				\
	--disable-directfb			\
	--disable-enca				\
	--disable-libdv				\
	--disable-lirc				\
	--disable-musepack			\
	--disable-openal			\
	--disable-ossaudio			\
	--disable-select			\
	--disable-smb				\
	--enable-runtime-cpudetection		\
	--extra-cflags="%{rpmcflags}"		\
	--extra-ldflags="%{rpmldflags}"		\
	--language=en,de,pl			\
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mplayer
%{_desktopdir}/*.desktop
%{_mandir}/man1/mplayer.1*

