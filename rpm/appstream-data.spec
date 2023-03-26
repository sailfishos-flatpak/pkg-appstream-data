Summary:   Fedora AppStream metadata
Name:      appstream-data
Version:   39
Release:   0
BuildArch: noarch
License:   CC0-1.0 AND CC-BY-1.0 AND CC-BY-SA-1.0 AND GFDL-1.1-or-later
URL:       https://github.com/hughsie/appstream-glib
Source0:   %{name}-%{version}.tar.bz2
Source1:   fedora-categories.xml

BuildRequires: libappstream-glib

%description
This package provides the distribution specific AppStream metadata required
for the GNOME and KDE software centers.

%install

DESTDIR=%{buildroot} appstream-util install \
	%{SOURCE1}

%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/*
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/xmls
