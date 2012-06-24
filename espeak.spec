#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	eSpeak - speech synthesizer for English and other languages
Summary(pl):	eSpeak - syntezator mowy dla j�zyka angielskiego i innych
Name:		espeak
Version:	1.17
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/espeak/%{name}-%{version}-source.zip
# Source0-md5:	b55432e1f0b7cea1276f25281714c771
Patch0:		%{name}-ac_am.patch
URL:		http://espeak.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	portaudio-devel >= 19
BuildRequires:	unzip
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	speak
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eSpeak is a software speech synthesizer for English and other
languages. eSpeak produces good quality English speech. It uses a
different synthesis method from other open source TTS engines, and
sounds quite different. It's perhaps not as natural or "smooth", but I
find the articulation clearer and easier to listen to for long
periods.
- It can run as a command line program to speak text from a file or
  from stdin. A library version is also available (isn't available in
  this package).
- Includes different Voices, whose characteristics can be altered.
- Can produce speech output as a WAV file.
- SSML (Speech Synthesis Markup Language) is supported (not complete),
  and also HTML.
- Compact size. The program and its data, including several languages,
  totals about 420 kbytes.
- Can translate text to phoneme codes, so it could be adapted as a
  front end for another speech synthesis engine.
- Potential for other languages. Several are included (e.g. Polish
  language) in varying stages of progress. Help from native speakers
  for these or other languages is welcomed.
- Development tools available for producing and tuning phoneme data.
- Written in C++.

It works well as a "Talker" with the KDE text to speech system (KTTS),
as an alternative to Festival for example. As such, it can speak text
which has been selected into the clipboard, or directly from the
Konquerer browser or the Kate editor.

%description -l pl
eSpeak to programowy syntezator mowy dla angielskiego i innych
j�zyk�w. Odtwarza angielsk� mow� dobrej jako�ci. U�ywa innej metody
syntezy ni� inne silniki TTS o otwartych �r�d�ach i brzmi troch�
inaczej. Nie jest mo�e tak naturalny czy "g�adki", ale autor uwa�a t�
wymow� za czystsz� i �atwiejsz� w s�uchaniu na d�u�sz� met�.

- Mo�e dzia�a� jako program z linii polece� do wymawiania tekstu z
  pliku lub standardowego wej�cia; dost�pna jest tak�e wersja w
  postaci biblioteki (nie w tym pakiecie).
- Zawiera r�ne g�osy, a ich charakterystyk� mo�na zmienia�.
- Potrafi tworzy� pliki WAV z mow�.
- Obs�ugiwany (ale nie w pe�ni) jest SSML (Speech Synthesis Markup
  Language)  oraz HTML.
- Ma�y rozmiar - program i jego dane, wraz z kilkoma j�zykami,
  mieszcz� si� w oko�o 420kB.
- Potrafi t�umaczy� tekst na kody fonem�w, wi�c mo�e by� zaadaptowany
  jako frontend dla innych silnik�w syntezy mowy.
- Potencjalnie mo�e nadawa� si� dla innych j�zyk�w; kilka jest
  do��czonych (na przyk�ad j.polski) w r�nym stadium zaawansowania.
  Mile widziana jest pomoc od os�b, dla kt�rych s� to j�zyki ojczyste.
- Dost�pne s� narz�dzia programistyczne do tworzenia i dostrajania
  danych dla fonem�w.
- Napisany w C++.

Dobrze pracuje jako "m�wca" z systemem przetwarzania tekstu na mow�
KDE (KTTS), na przyk�ad, jako alternatywa dla Festivala. Jako taki,
mo�e czyta� na g�os tekst zaznaczony uprzednio do schowka lub
bezpo�rednio z przegl�darki Konqueror i edytora Kate.

%package libs
Summary:	eSpeak shared libraries
Summary(pl):	eSpeak - biblioteki
Group:		Libraries
Obsoletes:	speak-libs

%description libs
eSpeak shared libraries.

%description libs -l pl
eSpeak - biblioteki dzielone.

%package devel
Summary:	eSpeak - development files
Summary(pl):	eSpeak - pliki dla programist�w
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
eSpeak - development files.

%description devel -l pl
eSpeak - pliki dla programist�w.

%package static
Summary:	eSpeak - static libraries
Summary(pl):	eSpeak - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
eSpeak - static libraries.

%description static -l pl
eSpeak - biblioteki statyczne.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
# remove pernicious headers to avoid using them during build instead of /usr/include/portaudio.h system header
rm -f src/portaudio{18,19,}.h

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog ReadMe docs
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}-data
%dir %{_datadir}/%{name}-data/voices
%dir %{_datadir}/%{name}-data/voices/en
%{_datadir}/%{name}-data/voices/af
%{_datadir}/%{name}-data/voices/cy
%{_datadir}/%{name}-data/voices/de
%{_datadir}/%{name}-data/voices/default
%{_datadir}/%{name}-data/voices/el
%{_datadir}/%{name}-data/voices/en/en-rp-f
%{_datadir}/%{name}-data/voices/en/en-wm-f
%{_datadir}/%{name}-data/voices/en/en-n
%{_datadir}/%{name}-data/voices/en/en
%{_datadir}/%{name}-data/voices/en/en1
%{_datadir}/%{name}-data/voices/en/en2
%{_datadir}/%{name}-data/voices/en/en3
%{_datadir}/%{name}-data/voices/en/en4
%{_datadir}/%{name}-data/voices/en/en6
%{_datadir}/%{name}-data/voices/en/en7
%{_datadir}/%{name}-data/voices/en/en8
%{_datadir}/%{name}-data/voices/en/en-croak
%{_datadir}/%{name}-data/voices/en/en-f
%{_datadir}/%{name}-data/voices/en/en-rp
%{_datadir}/%{name}-data/voices/en/en-n-f
%{_datadir}/%{name}-data/voices/en/en-wm
%{_datadir}/%{name}-data/voices/eo
%{_datadir}/%{name}-data/voices/es
%{_datadir}/%{name}-data/voices/fi
%{_datadir}/%{name}-data/voices/it
%{_datadir}/%{name}-data/voices/nl
%{_datadir}/%{name}-data/voices/pl
%{_datadir}/%{name}-data/voices/pt
%{_datadir}/%{name}-data/voices/ru
%dir %{_datadir}/%{name}-data/soundicons
%{_datadir}/%{name}-data/af_dict
%{_datadir}/%{name}-data/config
%{_datadir}/%{name}-data/cy_dict
%{_datadir}/%{name}-data/de_dict
%{_datadir}/%{name}-data/en_dict
%{_datadir}/%{name}-data/eo_dict
%{_datadir}/%{name}-data/el_dict
%{_datadir}/%{name}-data/es_dict
%{_datadir}/%{name}-data/fi_dict
%{_datadir}/%{name}-data/it_dict
%{_datadir}/%{name}-data/nl_dict
%{_datadir}/%{name}-data/phondata
%{_datadir}/%{name}-data/phonindex
%{_datadir}/%{name}-data/phontab
%{_datadir}/%{name}-data/pl_dict
%{_datadir}/%{name}-data/pt_dict
%{_datadir}/%{name}-data/ru_dict

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
