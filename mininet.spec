%define build_timestamp %(date +"%Y%m%d")
%define repo_url https://github.com/mininet/mininet
%define commit_id 1969669f510a7443f58b27b1640884b06b6867d4

Name: mininet
Version: 1.3.0d4
Release: %{build_timestamp}%{?dist}
Summary: Emulator for rapid prototyping of Software Defined Networks
License: GPL2
URL: https://github.com/mininet/mininet
Source0: %{repo_url}
BuildRequires: gcc make openssl-devel autoconf automake git
Requires: openssl

%description
Summary: Emulator for rapid prototyping of Software Defined Networks


%prep
if [ ! -d "%{SOURCE0}" ]; then
	git clone %{repo_url} %{SOURCE0}
fi

if [ ! -d "mininet" ]; then
	git clone %{SOURCE0}
fi
cd mininet
git checkout %{commit_id}

%build
cd mininet
make %{?_smp_mflags}

%install
cd mininet
%make_install

