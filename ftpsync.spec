Name:		ftpsync
Version:	1.81
Release:	%mkrel 1
Summary:	Tool to synchronize a remote FTP-served with a local directory
Source0:	http://www.linux-france.org/prj/ftpsync/dist/%{name}-%{version}.tgz
License:	GPLv2
Group:		Networking/File transfer
Url:		http://www.linux-france.org/prj/ftpsync/
BuildArch:	noarch

%description
The command ftpsync is a tool allowing incremental and recursive FTP
transfer from a local directory to a remote FTP-served directory.

We sometimes need to mirror a set of files on a remote ftp server. The
perfect tool (rsync) is not always available.

Developing a script invoking a standard FTP client software will cause
useless transfers (all files again and again even if they have not
changed), and taking sub-directories into account will not be easy.

ftpsync is the adequate tool because it reduces the amount of data
transferred by not transferring a given local file if the remote copy
has an newer date (so the copy is already done and up to date) and the
same size (transfer completely done). The difference between system
clocks is taken into account using the ftp protocol. ftpsync is
somewhat "like" the rsync command but it uses the FTP protocol and
only transfers local files to a remote FTP server. Moreover it
implements the missing 'recursive PUT' FTP command.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__install -m 755 ftpsync %{buildroot}%{_bindir}/ftpsync

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README VERSION GPL INSTALL TODO ChangeLog CREDITS
%{_bindir}/ftpsync

