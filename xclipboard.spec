Name:		xclipboard
Version:	1.1.2
Release:	1
Summary:	X clipboard client
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(xt)
BuildRequires: xaw-devel
BuildRequires: x11-util-macros >= 1.0.1

%description
The xclipboard program is used to collect and display text selections that are
sent to the clipboard by other clients. It is typically used to save clipboard
selections for later use. It stores each clipboard selection as a separate
string, each of which can be selected. Each time clipboard is asserted by
another application, xclipboard transfers the contents of that selection to a
new buffer and displays it in the text window.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xclipboard
%{_bindir}/xcutsel
%{_datadir}/X11/app-defaults/XClipboard
%{_mandir}/man1/xclipboard.*
%{_mandir}/man1/xcutsel.*


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1
+ Revision: 781021
- version update 1.1.2

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 671282
- mass rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464650
- New version: 1.1.0

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.1-9mdv2009.1
+ Revision: 366607
- no more autoconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 226019
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-7mdv2008.1
+ Revision: 155954
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-6mdv2008.0
+ Revision: 76406
- rebuild for 2008
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not harcode man page extension

