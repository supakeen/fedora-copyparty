Name:           copyparty
Version:        1.19.16
Release:        5%{?dist}
Summary:        Portable fileserver with many supported protocols

License:        MIT
URL:            https://github.com/9001/copyparty
Source:         %{url}/releases/download/v%{version}/copyparty-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)


Requires:       python3dist(qrcodegen)
Requires:       python3dist(ifaddr)
Requires:       python3dist(dnslib)

# Test requirements are generally the same as those needed
# for runtime.
BuildRequires:  python3dist(qrcodegen)

# On-the-fly certificate generation when available
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

# Upstream vendors certain Python libraries but has made it possible in the
# 1.19.16 release [1] to unvendor them. Let's do that.
# [1]: https://github.com/9001/copyparty/releases/tag/v1.19.16

# Only vendored for size see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/qrcodegen.py

# Only vendored for Python 2 support, see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/surrogateescape.py

# Only vendored (and upstream patched) for Python 2 support, see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/ifaddr

# Vendored (and upstream patched) for an Avahi bug, see [1]
# [1]: https://github.com/9001/copyparty/issues/887#issuecomment-3368299632
rm -rf copyparty/stolen/dnslib

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
* Sat Oct 11 2025 Simon de Vlieger <cmdr@supakeen.com> - 1.19.16-5
- Initial build
