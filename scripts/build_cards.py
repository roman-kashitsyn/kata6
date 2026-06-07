#!/usr/bin/env python3
"""Build cards.pdf from cards.typ using a pinned Typst binary.

On first run, downloads the pinned Typst release into .bin/
and verifies its SHA-256 against a hard-coded digest.
Subsequent runs reuse the cached binary
"""

from __future__ import annotations

import argparse
import hashlib
import platform
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

TYPST_VERSION = "0.14.2"

# SHA-256 digests from GitHub Release API (`digest` field on each asset)
# for tag v{TYPST_VERSION}. Update both this map and TYPST_VERSION together.
TYPST_ASSETS: dict[tuple[str, str], tuple[str, str]] = {
    # (sys.platform, machine): (archive name, sha256)
    ("darwin", "arm64"): (
        "typst-aarch64-apple-darwin.tar.xz",
        "470aa49a2298d20b65c119a10e4ff8808550453e0cb4d85625b89caf0cedf048",
    ),
    ("darwin", "x86_64"): (
        "typst-x86_64-apple-darwin.tar.xz",
        "4e91d8e1e33ab164f949c5762e01ee3faa585c8615a2a6bd5e3677fa8506b249",
    ),
    ("linux", "x86_64"): (
        "typst-x86_64-unknown-linux-musl.tar.xz",
        "a6044cbad2a954deb921167e257e120ac0a16b20339ec01121194ff9d394996d",
    ),
    ("linux", "aarch64"): (
        "typst-aarch64-unknown-linux-musl.tar.xz",
        "491b101aa40a3a7ea82a3f8a6232cabb4e6a7e233810082e5ac812d43fdcd47a",
    ),
}

DOWNLOAD_TIMEOUT_S = 60


def find_repo_root() -> Path:
    for p in [
        Path.cwd().resolve(),
        *Path.cwd().resolve().parents,
    ]:
        if (p / "cards.typ").exists() and (
            p / "src"
        ).is_dir():
            return p
    sys.exit(
        "could not find cards.typ and src/ — run from the kata6 repo"
    )


def asset_for_host() -> tuple[str, str]:
    key = (sys.platform, platform.machine())
    if key not in TYPST_ASSETS:
        sys.exit(
            f"unsupported host {key}; supported: {sorted(TYPST_ASSETS)}"
        )
    return TYPST_ASSETS[key]


def download_and_verify(
    url: str, expected_sha: str, dest: Path
) -> None:
    print(f"  fetching {url}", file=sys.stderr)
    dest.parent.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha256()
    with (
        urllib.request.urlopen(
            url, timeout=DOWNLOAD_TIMEOUT_S
        ) as resp,
        dest.open("wb") as out,
    ):
        while chunk := resp.read(1 << 16):
            sha.update(chunk)
            out.write(chunk)
    got = sha.hexdigest()
    if got != expected_sha:
        dest.unlink(missing_ok=True)
        sys.exit(
            f"sha256 mismatch for {url}\n  expected {expected_sha}\n  got      {got}"
        )


def ensure_typst(bin_root: Path) -> Path:
    typst_bin = bin_root / "typst"
    if typst_bin.exists():
        return typst_bin

    archive_name, expected_sha = asset_for_host()
    url = (
        f"https://github.com/typst/typst/releases/download/"
        f"v{TYPST_VERSION}/{archive_name}"
    )
    archive_path = bin_root / archive_name

    print(
        f"installing typst {TYPST_VERSION} into {bin_root}",
        file=sys.stderr,
    )
    download_and_verify(url, expected_sha, archive_path)

    with tarfile.open(archive_path, "r:xz") as tf:
        # Releases extract into a single top-level dir like typst-<triple>/.
        for member in tf.getmembers():
            name = Path(member.name).name
            if name == "typst" and member.isfile():
                member.name = "typst"
                tf.extract(member, bin_root, filter="data")
                break
        else:
            sys.exit(
                f"no typst binary inside {archive_name}"
            )

    typst_bin.chmod(0o755)
    archive_path.unlink()
    return typst_bin


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build cards.pdf from cards.typ using a pinned Typst binary."
    )
    parser.add_argument(
        "--font",
        help=(
            "Override the card font name. "
            "Default: DejaVu Sans Mono (embedded in Typst, fully reproducible). "
            "Setting this re-enables system font search so the name can be resolved."
        ),
    )
    parser.add_argument(
        "--font-path",
        help="Extra directory to search for fonts (e.g. ./fonts).",
    )
    args = parser.parse_args()

    repo_root = find_repo_root()
    bin_root = repo_root / ".bin" / f"typst-{TYPST_VERSION}"

    slugs = sorted(
        p.stem for p in (repo_root / "src").glob("*.py")
    )
    if not slugs:
        sys.exit("no algorithms found in src/*.py")

    typst = ensure_typst(bin_root)
    out = repo_root / "cards.pdf"
    cmd = [
        str(typst),
        "compile",
        "cards.typ",
        str(out),
        "--root",
        ".",
        "--input",
        f"slugs={','.join(slugs)}",
    ]
    if args.font:
        cmd += ["--input", f"font={args.font}"]
    else:
        cmd.append("--ignore-system-fonts")
    if args.font_path:
        cmd += ["--font-path", args.font_path]
    print(f"$ {' '.join(cmd)}", file=sys.stderr)
    return subprocess.call(cmd, cwd=repo_root)


if __name__ == "__main__":
    raise SystemExit(main())
