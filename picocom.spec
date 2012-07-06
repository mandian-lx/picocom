Name:           picocom
Version:        1.7
Release:        1
Summary:        Minimal serial communications program

Group:          Communications
License:        GPLv2+
URL:            http://code.google.com/p/picocom/
Source0:        http://picocom.googlecode.com/files/picocom-%{version}.tar.gz

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

%prep
%setup -q

%build
make CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS" %{_smp_mflags} UUCP_LOCK_DIR=/run/lock/picocom

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
install -m 755 picocom %{buildroot}%{_bindir}/
install -m 644 picocom.8 %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}/run/lock/picocom

%pre
getent group dialout >/dev/null || groupadd -g 18 -r -f dialout
exit 0

%files
%doc CHANGES CONTRIBUTORS LICENSE.txt README
%dir %attr(0775,root,dialout) /run/lock/picocom
%{_bindir}/picocom
%{_mandir}/man8/*
