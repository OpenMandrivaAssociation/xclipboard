Name:		xclipboard
Version:	1.1.6
Release:	1
Summary:	X clipboard client
Group:		Development/X11
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildSystem:   autotools

BuildRequires: libtool-base
BuildRequires: slibtool
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


%files
%{_bindir}/xclipboard
%{_bindir}/xcutsel
%{_datadir}/X11/app-defaults/XClipboard
%{_mandir}/man1/xclipboard.*
%{_mandir}/man1/xcutsel.*
