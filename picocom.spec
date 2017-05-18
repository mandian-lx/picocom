Summary:        Minimal dumb-terminal emulation program
Name:           picocom
Version:        2.2
Release:        1
License:        GPLv2+
Group:          Communications
URL:            https://github.com/npat-efault/picocom
Source0:        https://github.com/npat-efault/picocom/archive/%{version}/%{name}-%{version}.tar.gz

# for groupadd
Requires(pre):  shadow-utils

%description
As its name suggests, [picocom] is a minimal dumb-terminal emulation
program. It is, in principle, very much like minicom, only it's "pico"
instead of "mini"! It was designed to serve as a simple, manual, modem
configuration, testing, and debugging tool. It has also served (quite
well) as a low-tech "terminal-window" to allow operator intervention
in PPP connection scripts (something like the ms-windows "open
terminal window before / after dialing" feature).  It could also prove
useful in many other similar tasks. It is ideal for embedded systems
since its memory footprint is minimal (less than 20K, when
stripped).

%files
%{_bindir}/picocom
%{_mandir}/man1/*
%dir %attr(0775,root,dialout) /run/lock/picocom
%doc README.md
%doc TODO
%doc CONTRIBUTORS
%doc CHANGES.old
%doc LICENSE.txt

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%setup_compile_flags
%make  CFLAGS="%{optflags}" CPPFLAGS="%{optflags}" LDLIBS="%{ldflags}" UUCP_LOCK_DIR=/run/lock/picocom

%install
# binary
install -dm 0755 %{buildroot}%{_bindir}/
install -pm 0755 picocom %{buildroot}%{_bindir}/

# manpage
install -dm 0755 %{buildroot}%{_mandir}/man1/
install -pm 644 picocom.1 %{buildroot}%{_mandir}/man1/

install -dm 0755 %{buildroot}/run/lock/picocom

%pre
getent group dialout >/dev/null || groupadd -g 18 -r -f dialout
exit 0

