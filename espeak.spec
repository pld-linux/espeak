Summary:	eSpeak - speech synthesizer for English and other languages
Summary(pl.UTF-8):	eSpeak - syntezator mowy dla języka angielskiego i innych
Name:		espeak
Version:	1.24
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/espeak/%{name}-%{version}-source.zip
# Source0-md5:	6b00c634a18caca91e8c94ca36675304
Patch0:		%{name}-Makefile.patch
URL:		http://espeak.sourceforge.net/
BuildRequires:	libstdc++-devel
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

%description -l pl.UTF-8
eSpeak to programowy syntezator mowy dla angielskiego i innych
języków. Odtwarza angielską mowę dobrej jakości. Używa innej metody
syntezy niż inne silniki TTS o otwartych źródłach i brzmi trochę
inaczej. Nie jest może tak naturalny czy "gładki", ale autor uważa tę
wymowę za czystszą i łatwiejszą w słuchaniu na dłuższą metę.

- Może działać jako program z linii poleceń do wymawiania tekstu z
  pliku lub standardowego wejścia; dostępna jest także wersja w
  postaci biblioteki (nie w tym pakiecie).
- Zawiera różne głosy, a ich charakterystykę można zmieniać.
- Potrafi tworzyć pliki WAV z mową.
- Obsługiwany (ale nie w pełni) jest SSML (Speech Synthesis Markup
  Language)  oraz HTML.
- Mały rozmiar - program i jego dane, wraz z kilkoma językami,
  mieszczą się w około 420kB.
- Potrafi tłumaczyć tekst na kody fonemów, więc może być zaadaptowany
  jako frontend dla innych silników syntezy mowy.
- Potencjalnie może nadawać się dla innych języków; kilka jest
  dołączonych (na przykład j.polski) w różnym stadium zaawansowania.
  Mile widziana jest pomoc od osób, dla których są to języki ojczyste.
- Dostępne są narzędzia programistyczne do tworzenia i dostrajania
  danych dla fonemów.
- Napisany w C++.

Dobrze pracuje jako "mówca" z systemem przetwarzania tekstu na mowę
KDE (KTTS), na przykład, jako alternatywa dla Festivala. Jako taki,
może czytać na głos tekst zaznaczony uprzednio do schowka lub
bezpośrednio z przeglądarki Konqueror i edytora Kate.

%package libs
Summary:	eSpeak shared libraries
Summary(pl.UTF-8):	eSpeak - biblioteki
Group:		Libraries
Obsoletes:	speak-libs

%description libs
eSpeak shared libraries.

%description libs -l pl.UTF-8
eSpeak - biblioteki dzielone.

%package devel
Summary:	eSpeak - development files
Summary(pl.UTF-8):	eSpeak - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
eSpeak - development files.

%description devel -l pl.UTF-8
eSpeak - pliki dla programistów.

%package static
Summary:	eSpeak - static libraries
Summary(pl.UTF-8):	eSpeak - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
eSpeak - static libraries.

%description static -l pl.UTF-8
eSpeak - biblioteki statyczne.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
# remove pernicious headers to avoid using them during build instead of /usr/include/portaudio.h system header
rm -f src/portaudio{18,19,}.h

%build
cd src
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \

%install
rm -rf $RPM_BUILD_ROOT

cd src
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR="%{_libdir}"

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
%{_datadir}/%{name}-data/voices/af
%{_datadir}/%{name}-data/voices/cs
%{_datadir}/%{name}-data/voices/cy
%{_datadir}/%{name}-data/voices/de
%{_datadir}/%{name}-data/voices/default
%{_datadir}/%{name}-data/voices/el
%dir %{_datadir}/%{name}-data/voices/en
%{_datadir}/%{name}-data/voices/en/en
%{_datadir}/%{name}-data/voices/en/en-n
%{_datadir}/%{name}-data/voices/en/en-r
%{_datadir}/%{name}-data/voices/en/en-sc
%{_datadir}/%{name}-data/voices/en/en-wm
%{_datadir}/%{name}-data/voices/en/en-croak
%{_datadir}/%{name}-data/voices/en/en-rp
%{_datadir}/%{name}-data/voices/eo
%{_datadir}/%{name}-data/voices/es
%{_datadir}/%{name}-data/voices/fi
%{_datadir}/%{name}-data/voices/fr
#%%{_datadir}/%{name}-data/voices/fr-ca
%{_datadir}/%{name}-data/voices/hi
%{_datadir}/%{name}-data/voices/hr
%{_datadir}/%{name}-data/voices/hu
%{_datadir}/%{name}-data/voices/it
%{_datadir}/%{name}-data/voices/nl
%{_datadir}/%{name}-data/voices/no
%{_datadir}/%{name}-data/voices/pl
%{_datadir}/%{name}-data/voices/pt
%{_datadir}/%{name}-data/voices/pt-pt
%{_datadir}/%{name}-data/voices/ro
%{_datadir}/%{name}-data/voices/ru
%{_datadir}/%{name}-data/voices/sk
%{_datadir}/%{name}-data/voices/sv
%{_datadir}/%{name}-data/voices/sw
%{_datadir}/%{name}-data/voices/vi
%{_datadir}/%{name}-data/voices/zhy
%dir %{_datadir}/%{name}-data/voices/mb
%{_datadir}/%{name}-data/voices/mb/mb-af1
%{_datadir}/%{name}-data/voices/mb/mb-af1-en
%{_datadir}/%{name}-data/voices/mb/mb-cr1
%{_datadir}/%{name}-data/voices/mb/mb-cz2
%{_datadir}/%{name}-data/voices/mb/mb-de4
%{_datadir}/%{name}-data/voices/mb/mb-de5
%{_datadir}/%{name}-data/voices/mb/mb-de4-en
%{_datadir}/%{name}-data/voices/mb/mb-de5-en
%{_datadir}/%{name}-data/voices/mb/mb-en1
%{_datadir}/%{name}-data/voices/mb/mb-fr1
%{_datadir}/%{name}-data/voices/mb/mb-fr1-en
%{_datadir}/%{name}-data/voices/mb/mb-fr4
%{_datadir}/%{name}-data/voices/mb/mb-fr4-en
%{_datadir}/%{name}-data/voices/mb/mb-hu1
%{_datadir}/%{name}-data/voices/mb/mb-hu1-en
%{_datadir}/%{name}-data/voices/mb/mb-nl2
%{_datadir}/%{name}-data/voices/mb/mb-nl2-en
%{_datadir}/%{name}-data/voices/mb/mb-pl1
%{_datadir}/%{name}-data/voices/mb/mb-pl1-en
%{_datadir}/%{name}-data/voices/mb/mb-ro1
%{_datadir}/%{name}-data/voices/mb/mb-ro1-en
%{_datadir}/%{name}-data/voices/mb/mb-sw1
%{_datadir}/%{name}-data/voices/mb/mb-sw1-en
%{_datadir}/%{name}-data/voices/mb/mb-sw2
%{_datadir}/%{name}-data/voices/mb/mb-sw2-en
%{_datadir}/%{name}-data/voices/mb/mb-us1
%{_datadir}/%{name}-data/voices/mb/mb-us2
%{_datadir}/%{name}-data/voices/mb/mb-us3
%dir %{_datadir}/%{name}-data/soundicons
%{_datadir}/%{name}-data/af_dict
%{_datadir}/%{name}-data/config
%{_datadir}/%{name}-data/cs_dict
%{_datadir}/%{name}-data/cy_dict
%{_datadir}/%{name}-data/de_dict
%{_datadir}/%{name}-data/en_dict
%{_datadir}/%{name}-data/eo_dict
%{_datadir}/%{name}-data/el_dict
%{_datadir}/%{name}-data/es_dict
%{_datadir}/%{name}-data/fi_dict
%{_datadir}/%{name}-data/fr_dict
%{_datadir}/%{name}-data/hi_dict
%{_datadir}/%{name}-data/hr_dict
%{_datadir}/%{name}-data/hu_dict
%{_datadir}/%{name}-data/it_dict
%{_datadir}/%{name}-data/nl_dict
%{_datadir}/%{name}-data/no_dict
%{_datadir}/%{name}-data/phondata
%{_datadir}/%{name}-data/phonindex
%{_datadir}/%{name}-data/phontab
%{_datadir}/%{name}-data/pl_dict
%{_datadir}/%{name}-data/pt_dict
%{_datadir}/%{name}-data/ro_dict
%{_datadir}/%{name}-data/ru_dict
%{_datadir}/%{name}-data/sk_dict
%{_datadir}/%{name}-data/sv_dict
%{_datadir}/%{name}-data/sw_dict
%{_datadir}/%{name}-data/vi_dict
%{_datadir}/%{name}-data/zhy_dict
%dir %{_datadir}/%{name}-data/mbrola_ph
%{_datadir}/%{name}-data/mbrola_ph/af1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/ca1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/cr1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/cs_phtrans
%{_datadir}/%{name}-data/mbrola_ph/de4_phtrans
%{_datadir}/%{name}-data/mbrola_ph/de5_phtrans
%{_datadir}/%{name}-data/mbrola_ph/en1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/fr1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/hu1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/nl_phtrans
%{_datadir}/%{name}-data/mbrola_ph/pl1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/ro1_phtrans
%{_datadir}/%{name}-data/mbrola_ph/sv_phtrans
%{_datadir}/%{name}-data/mbrola_ph/us3_phtrans
%{_datadir}/%{name}-data/mbrola_ph/us_phtrans
%dir %{_datadir}/%{name}-data/voices/!v
%{_datadir}/%{name}-data/voices/!v/!variant1
%{_datadir}/%{name}-data/voices/!v/!variant11
%{_datadir}/%{name}-data/voices/!v/!variant12
%{_datadir}/%{name}-data/voices/!v/!variant13
%{_datadir}/%{name}-data/voices/!v/!variant14
%{_datadir}/%{name}-data/voices/!v/!variant2
%{_datadir}/%{name}-data/voices/!v/!variant3
%{_datadir}/%{name}-data/voices/!v/!variant4
%{_datadir}/%{name}-data/voices/!v/!variant5
%{_datadir}/%{name}-data/voices/!v/!variant6

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
