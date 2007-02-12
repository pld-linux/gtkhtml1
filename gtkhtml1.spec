Summary:	Gtkhtml library
Summary(pl.UTF-8):   Biblioteka gtkhtml
Summary(pt_BR.UTF-8):   Biblioteca gtkhtml
Summary(ru.UTF-8):   GtkHTML - это библиотека рендеринга/редактирования HTML
Summary(uk.UTF-8):   GtkHTML - це бібліотека рендерингу/редагування HTML
Name:		gtkhtml1
%define	mver	1.1
Version:	%{mver}.10
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtkhtml/1.1/gtkhtml-%{version}.tar.bz2
# Source0-md5:	8647407560e4b61ba4a12653b9cc8869
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pixmap.patch
Patch2:		%{name}-get_default_fonts.patch
BuildRequires:	GConf-devel >= 1.0.7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.32
BuildRequires:	control-center1-devel >= 1.0.0
BuildRequires:	gal1-devel >= 0.21
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.8.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.29
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libghttp-devel >= 1.0
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Obsoletes:	libgtkhtml20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl.UTF-8
GtkHTML jesrt "lekką" bibiloteką do renderingu, drukowania i edycji
HTML. Pierwotne źródła tej biblioteki bazują na KHTMLW ale teraz
GtkHTML jest rozwijana niezależnie od KHTMLW,

%description -l pt_BR.UTF-8
Este é o GtkHTML, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru.UTF-8
Это GtkHTML, легкий "движок" рендеринга/печати/редактирования HTML.
Сначала он базировался на KHTMLW, но теперь разрабатывается
независимо.

%description -l uk.UTF-8
Це GtkHTML, легке ядро рендерингу/друку/редагування HTML. Воно
спочатку базувалось на KHTMLW, але тепер розробляється незалежно від
нього.

%package devel
Summary:	Header files and etc neccessary to develop gtkhtml applications
Summary(es.UTF-8):   Bibliotecas, archivos de inclusión, e etc. para desarrollar aplicaciones gtkhtml
Summary(pl.UTF-8):   Pliki nagłówkowe i inne nizbędne do tworzenia aplikacji używających gtkhtml
Summary(pt_BR.UTF-8):   Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações gtkhtml
Summary(ru.UTF-8):   Файлы, необходимые для разработки программ с использованием gtkhtml
Summary(uk.UTF-8):   Файли, необхідні для розробки програм з використанням gtkhtml
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf-devel >= 1.0.7
Requires:	bonobo-devel >= 0.32
Requires:	gal1-devel >= 0.21
Requires:	gdk-pixbuf-gnome-devel >= 0.8.0
Requires:	gnome-print-devel >= 0.29
Requires:	gtk-doc-common
Requires:	libglade-gnome-devel
Obsoletes:	lubgtkhtml20-devel

%description devel
Header files and etc neccessary to develop gtkhtml applications.

%description devel -l es.UTF-8
Bibliotecas, archivos de inclusión, y etc para desarrollar
aplicaciones gtkhtml.

%description devel -l pl.UTF-8
Pliki nagłówkowe i reszta niezbędnych przy tworzeniu aplikacji
wykorzystujacych gtkhtml.

%description devel -l pt_BR.UTF-8
Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações
gtkhtml.

%description devel -l ru.UTF-8
Файлы, необходимые для разработки программ с использованием gtkhtml.

%description devel -l uk.UTF-8
Файли, необхідні для розробки програм з використанням gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(es.UTF-8):   Bibliotecas estáticas para desarrollar aplicaciones gtkhtml
Summary(pl.UTF-8):   Biblioteki statyczne gtkhtml
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolver aplicações gtkhtml
Summary(ru.UTF-8):   Статические библиотеки для разработки программ с gtkhtml
Summary(uk.UTF-8):   Статичні бібліотеки для розробки програм з gtkhtml
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtkhtml libraries.

%description static -l es.UTF-8
Bibliotecas estáticas para desarrollar aplicaciones gtkhtml.

%description static -l pl.UTF-8
Biblioteki statyczne gtkhtml.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolver aplicações gtkhtml.

%prep
%setup -q -n gtkhtml-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/' configure.in
sed -i -e 's/AM_PROG_XML_I18N_TOOLS/AC_PROG_INTLTOOL/' configure.in
sed -i -e 's/XML_I18N_MERGE_OAF_RULE/INTLTOOL_OAF_RULE/' \
	components/{html-editor,ebrowser}/Makefile.am
sed -i -e 's/nn no pl/nn nb pl/' configure.in

mv -f po/{no,nb}.po

%build
%{__libtoolize}
intltoolize --force
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
export GNOME_LIBCONFIG_PATH=%{_libdir}
%configure \
	--with-bonobo \
	--with-gconf

%{__make} \
	idldir=%{_datadir}/idl \
	pkgconfigdir=%{_pkgconfigdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_desktopdir} \
	pkgconfigdir=%{_pkgconfigdir} \
	idldir=%{_datadir}/idl \
	HTML_DIR=%{_gtkdocdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/plugin/*.{la,a}

%find_lang gtkhtml --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gtkhtml.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgtkhtml-1.1.so.*.*.*
%attr(755,root,root) %{_libdir}/bonobo/plugin/lib*.so
%dir %{_datadir}/gtkhtml-%{mver}
%{_datadir}/gtkhtml-%{mver}/icons
%{_datadir}/gtkhtml-%{mver}/keybindingsrc*
%{_datadir}/gtkhtml-%{mver}/*.glade
%{_datadir}/control-center/Documents/*
%{_datadir}/gnome/ui/*
%{_datadir}/oaf/*.oaf
%{_datadir}/idl/*.idl
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-1.1.so
%{_libdir}/libgtkhtml-1.1.la
%{_includedir}/gtkhtml-1.1
%{_pkgconfigdir}/gtkhtml-1.1.pc
%{_gtkdocdir}/gtkhtml*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtml-1.1.a
