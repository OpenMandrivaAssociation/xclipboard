Name:		xclipboard
Version:	1.0.1
Release:	%mkrel 6
Summary:	X clipboard client
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

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
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xclipboard
%{_bindir}/xcutsel
%{_datadir}/X11/app-defaults/XClipboard
%{_mandir}/man1/xclipboard.*
%{_mandir}/man1/xcutsel.*


