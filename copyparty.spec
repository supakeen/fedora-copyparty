Name:           copyparty
Version:        1.19.15
Release:        0%{?dist}
Summary:        Portable fileserver with many supported protocols

License:        MIT
URL:            https://github.com/9001/copyparty
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(pytest)

%global _description %{expand:
Portable file server with accelerated resumable uploads, deduplication, WebDAV, FTP, zeroconf, media indexer, video thumbnails, audio transcoding, and write-only folders
}

%description %_description

%package -n copyparty-u2c
Summary: upload2copyparty client application.

%description -n copyparty-u2c %_description

%package -n copyparty-partyfuse
Requires: python3dist(fusepy)

Summary: Mount a copyparty instance through FUSE

%description -n copyparty-partyfuse %_description

%prep
%autosetup -p1 -n copyparty-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files copyparty

%check
%pytest

%files -n copyparty -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/copyparty
%{_docdir}/copyparty/LICENSE

%files -n copyparty-u2c
%{_bindir}/u2c
%{_bindir}/u2c.py

%files -n copyparty-partyfuse
%{_bindir}/partyfuse
%{_bindir}/partyfuse.py

%changelog
* Thu Jul 31 2025 Simon de Vlieger <cmdr@supakeen.com> - 1.18.8-0
- Initial build
