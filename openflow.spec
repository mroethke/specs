%define build_timestamp %(date +"%Y%m%d")
%define repo_url https://github.com/mininet/openflow

Name: openflow
Version: master
Release: %{build_timestamp}%{?dist}
Summary: OpenFlow is a flow-based switch specification designed to enable researchers to run experiments in live networks.
License: GPL2
URL: https://github.com/mininet/openflow
Source0: %{repo_url}
BuildRequires: gcc make openssl-devel autoconf automake git
Requires: openssl

%description
OpenFlow is a flow-based switch specification designed to enable researchers to run experiments in live networks.


%prep
if [ ! -d "%{SOURCE0}" ]; then
	git clone %{repo_url} %{SOURCE0}
fi

if [ ! -d "openflow" ]; then
	git clone %{SOURCE0}
fi

%build
ls
cd openflow
./boot.sh
%configure
make %{?_smp_mflags}

%install
cd openflow
%make_install

%files
/usr/bin/controller
/usr/bin/dpctl
/usr/bin/ofdatapath
/usr/bin/ofp-discover
/usr/bin/ofp-kill
/usr/bin/ofp-pki
/usr/bin/ofprotocol
/usr/bin/vlogconf
/usr/share/man/man8/controller.8.gz
/usr/share/man/man8/dpctl.8.gz
/usr/share/man/man8/ofdatapath.8.gz
/usr/share/man/man8/ofp-discover.8.gz
/usr/share/man/man8/ofp-kill.8.gz
/usr/share/man/man8/ofp-pki.8.gz
/usr/share/man/man8/ofprotocol.8.gz
/usr/share/man/man8/vlogconf.8.gz
/usr/share/openflow/commands/reboot

