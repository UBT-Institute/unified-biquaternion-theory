#!/usr/bin/env python3
"""Build three deterministic, commit-bound ZIP distributions from tracked Git blobs.

Core and Research are curated source profiles, not standalone build promises.
Full preserves all tracked paths (including export-ignored files), not Git history.
The ordinary git archive and its portable manifests remain unchanged.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import stat
import subprocess
import zipfile

MIB = 1024 * 1024
LIMITS = {"core": 12*MIB, "research": 24*MIB, "full": 64*MIB}
EXTRA_ROOTS = {"research_tracks", "research_fronts", "speculative_extensions",
               "ARCHIVE", "projects", "experiments", "DATA", "reports"}
HISTORY = {"ARCHIVE", "archive_legacy", "legacy_variants"}
MANIFESTS = {"SHA256SUMS.txt", "SHA256SUMS_PDFS.txt",
             "PROVENANCE_INVENTORY_2026-08-01.txt"}
INDEX = ".ubt-distribution.json"

def git(*args):
    return subprocess.check_output(["git", *args])

def entries(commit):
    result = {}
    for entry in git("ls-tree", "-r", "-z", commit).split(b"\0"):
        if not entry:
            continue
        meta, name = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        path = name.decode("utf-8")
        parts = PurePosixPath(path).parts
        if not parts or path.startswith("/") or ".." in parts or "\\" in path or path == INDEX:
            raise ValueError(f"Unsafe or reserved path: {path!r}")
        if kind != "blob":
            raise ValueError(f"Unsupported Git object {kind}: {path}")
        result[path] = (mode, oid)
    return result

def included(path, profile, source_paths):
    if profile == "full":
        return True
    parts = PurePosixPath(path).parts
    if path not in source_paths or path in MANIFESTS or HISTORY.intersection(parts):
        return False
    return profile == "research" or parts[0] not in EXTRA_ROOTS

def write_zip(path, commit, profile, files, source_paths, blob):
    inventory = []
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        def add(name, data, mode):
            info = zipfile.ZipInfo(name, (1980,1,1,0,0,0))
            info.create_system = 3
            info.external_attr = mode << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data, compresslevel=9)
        for name, (mode, oid) in sorted(files.items()):
            if not included(name, profile, source_paths):
                continue
            data = blob(oid)
            add(name, data, int(mode, 8))
            inventory.append({"path": name, "sha256": hashlib.sha256(data).hexdigest(),
                              "bytes": len(data), "git_mode": mode})
        add(INDEX, (json.dumps({"schema":1,"commit":commit,"profile":profile,
                                "files":inventory}, ensure_ascii=False,
                               sort_keys=True, indent=2)+"\n").encode(), stat.S_IFREG | 0o644)
    verify_zip(path, commit, profile, files, source_paths)
    return path.stat().st_size

def verify_zip(path, commit, profile, files, source_paths):
    with zipfile.ZipFile(path) as z:
        index = json.loads(z.read(INDEX))
        expected = {p for p in files if included(p, profile, source_paths)}
        actual = {f["path"] for f in index["files"]}
        if (index["commit"], index["profile"]) != (commit, profile):
            raise ValueError("Wrong archive identity")
        if expected != actual or len(actual) != len(index["files"]) or set(z.namelist()) != actual | {INDEX} or len(z.namelist()) != len(actual)+1:
            raise ValueError("Incomplete or duplicate archive membership")
        for item in index["files"]:
            name = item["path"]
            data = z.read(name)
            if (len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]
                or item["git_mode"] != files[name][0]
                or z.getinfo(name).external_attr >> 16 != int(files[name][0], 8)):
                raise ValueError(f"Integrity mismatch: {name}")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    commit = git("rev-parse", "--verify", args.ref+"^{commit}").decode().strip()
    files = entries(commit)
    with zipfile.ZipFile(io.BytesIO(git("archive","--format=zip",commit))) as source:
        source_paths = {i.filename for i in source.infolist() if not i.is_dir()}
    args.out.mkdir(parents=True, exist_ok=True)
    # Stream Git blobs in one persistent subprocess to avoid thousands of launches.
    failed = []
    with subprocess.Popen(["git","cat-file","--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
        def blob(oid):
            proc.stdin.write((oid+"\n").encode()); proc.stdin.flush()
            header = proc.stdout.readline().decode().split()
            if len(header)!=3 or header[0]!=oid or header[1]!="blob":
                raise ValueError(f"Unexpected blob response: {header}")
            data = proc.stdout.read(int(header[2]))
            if len(data)!=int(header[2]) or proc.stdout.read(1)!=b"\n":
                raise ValueError("Truncated blob")
            return data
        try:
            for profile, limit in LIMITS.items():
                target = args.out / f"UBT-{profile}.zip"
                size = write_zip(target,commit,profile,files,source_paths,blob)
                print(f"{profile}: {size} bytes / {limit} bytes")
                if size > limit:
                    failed.append(profile)
        finally:
            proc.stdin.close()
    if failed:
        raise SystemExit("Distribution size limit exceeded: "+", ".join(failed))

if __name__ == "__main__":
    main()
