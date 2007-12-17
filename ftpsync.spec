%define name 	ftpsync
%define version 1.80
%define release %mkrel 1

Summary: Synchronize a remote arborescence from a local directory by using FTP
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: http://www.linux-france.org/prj/ftpsync/dist/%{name}-%{version}.tar.bz2
License: GPL
Group: 	 Networking/File transfer
Url: 	 http://www.linux-france.org/prj/ftpsync/
Patch0:	%{name}-Makefile.patch.bz2
BuildArch:	noarch

Requires:	perl

%description

The command ftpsync is a tool allowing incremental and recursive FTP
transfer from a local directory to a remote FTP-served directory.

We sometimes need to mirror a set of files on a remote ftp server. The
perfect tool (rsync) is not always available.

Developing a script invoking a standard FTP client software will cause
useless transfers (all files again and again even if they have not
changed), and taking subdirectories into account will not be easy.

ftpsync is the adequate tool because it reduces the amount of data
transfered by not transfering a given local file if the remote copy
has an newer date (so the copy is already done and up to date) and the
same size (transfert completely done). The difference between system
clocks is taken into account using the ftp protocol. ftpsync is
somewhat "like" the rsync command but it uses the FTP protocol and
only transfers local files to a remote FTP server. Moreover it
implements the missing 'recursive PUT' FTP command.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -f ftpsync $RPM_BUILD_ROOT/%{_bindir}
chmod 0755 $RPM_BUILD_ROOT/%{_bindir}/ftpsync
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
cp -f README VERSION GPL INSTALL TODO ChangeLog CREDITS $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README VERSION GPL INSTALL TODO ChangeLog CREDITS
%{_bindir}/ftpsync

