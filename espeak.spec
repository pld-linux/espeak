Summary:	eSpeak - speech synthesizer for English and other languages
Summary(pl.UTF-8):	eSpeak - syntezator mowy dla języka angielskiego i innych
Name:		espeak
Version:	1.46.02
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/espeak/%{name}-%{version}-source.zip
# Source0-md5:	84e8e44562f05a3afc5427218afc8af1
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
  language) in varying stages of progress. Help from native speakers for
  these or other languages is welcomed.
- Development tools available for producing and tuning phoneme data.
- Written in C++.

It works well as a "Talker" with the KDE text to speech system (KTTS),
as an alternative to Festival for example. As such, it can speak text
which has been selected into the clipboard, or directly from the
Konquerer browser or the Kate editor.

%description -l pl.UTF-8
eSpeak to programowy syntezator mowy dla angielskiego i innych
języków. Odtwarza angielską mowę dobrej jakości. Używa innej
metody syntezy niż inne silniki TTS o otwartych źródłach i brzmi
trochę inaczej. Nie jest może tak naturalny czy "gładki", ale autor
uważa tę wymowę za czystszą i łatwiejszą w słuchaniu na
dłuższą metę.

- Może działać jako program z linii poleceń do wymawiania tekstu z
  pliku lub standardowego wejścia; dostępna jest także wersja w
  postaci biblioteki (nie w tym pakiecie).
- Zawiera różne głosy, a ich charakterystykę można zmieniać.
- Potrafi tworzyć pliki WAV z mową.
- Obsługiwany (ale nie w pełni) jest SSML (Speech Synthesis Markup
  Language) oraz HTML.
- Mały rozmiar - program i jego dane, wraz z kilkoma językami,
  mieszczą się w około 420kB.
- Potrafi tłumaczyć tekst na kody fonemów, więc może być
  zaadaptowany jako frontend dla innych silników syntezy mowy.
- Potencjalnie może nadawać się dla innych języków; kilka jest
  dołączonych (na przykład j.polski) w różnym stadium
  zaawansowania. Mile widziana jest pomoc od osób, dla których są to
  języki ojczyste.
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
# remove pernicious headers to avoid using them during build instead of %{_includedir}/portaudio.h system header
%{__rm} src/portaudio{18,19,}.h

%ifarch sparc64
sed -i -e 's/-fpic/-fPIC/g' src/Makefile
%endif

%build
%{__make} -C src \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR="%{_libdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt ReadMe docs
%attr(755,root,root) %{_bindir}/espeak
%{_datadir}/%{name}-data

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libespeak.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libespeak.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libespeak.so
%{_includedir}/espeak

%files static
%defattr(644,root,root,755)
%{_libdir}/libespeak.a
