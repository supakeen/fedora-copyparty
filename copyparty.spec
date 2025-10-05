Name:           copyparty
Version:        1.19.15
Release:        3%{?dist}
Summary:        Portable fileserver with many supported protocols

License:        MIT
URL:            https://github.com/9001/copyparty
Source:         %{url}/releases/download/v%{version}/copyparty-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

Recommends:     golang-github-cloudflare-cfssl

# Thumbnailing, media indexing, and audio transcoding functionality
Recommends:     python3-pillow
Recommends:     ffmpeg

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

%files -n copyparty-u2c
%{_bindir}/u2c

%files -n copyparty-partyfuse
%{_bindir}/partyfuse

%changelog
* Sun Oct 5 2025 Simon de Vlieger <cmdr@supakeen.com> - 1.19.15-3
- Initial build
