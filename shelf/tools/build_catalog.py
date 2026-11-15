#!/usr/bin/env python3
"""Builds shelf/catalog.json from shelf/titles.json.

    python shelf/tools/build_catalog.py           # download every ROM, hash, write catalog.json
    python shelf/tools/build_catalog.py --verify  # re-download what catalog.json points at and check

titles.json is the hand-maintained source of truth (everything except sha256
and size). This script downloads each entry's downloadURL into a temp folder,
records the byte size and sha256 of the exact file, checks the extension and
the ROM header looks right for the system, and writes catalog.json. Entries
whose downloadURL points into this repository (shelf/roms/...) are hashed
from the local file so the catalogue never describes a file that is not
committed. Nothing here needs more than the standard library.
"""
import hashlib
import json
import os
import sys
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SHELF = os.path.dirname(HERE)
RAW_BASE = 'https://raw.githubusercontent.com/RedfernsOutpost/tinbox-support/main/shelf/'
UA = 'tinbox-support shelf builder (+https://github.com/RedfernsOutpost/tinbox-support)'

REQUIRED = ['id', 'title', 'author', 'system', 'year', 'blurb', 'licence', 'licenceURL',
            'sourceURL', 'downloadURL', 'cover', 'licenceFile', 'fileName', 'tags']


def fetch(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, 'wb') as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def header_ok(path, system):
    with open(path, 'rb') as f:
        data = f.read(0x200)
    if system == 'gba':
        # Fixed byte 0x96 at 0xB2 in every GBA header.
        return len(data) > 0xB2 and data[0xB2] == 0x96
    # Game Boy: the Nintendo logo starts at 0x104 with CE ED 66 66.
    return len(data) > 0x108 and data[0x104:0x108] == bytes.fromhex('CEED6666')


def local_path_for(url):
    if url.startswith(RAW_BASE):
        return os.path.join(SHELF, url[len(RAW_BASE):].replace('/', os.sep))
    return None


def build(verify=False):
    with open(os.path.join(SHELF, 'titles.json'), encoding='utf-8') as f:
        source = json.load(f)
    existing = {}
    if verify:
        with open(os.path.join(SHELF, 'catalog.json'), encoding='utf-8') as f:
            existing = {t['id']: t for t in json.load(f)['titles']}

    out, problems = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for entry in source['titles']:
            missing = [k for k in REQUIRED if k not in entry]
            if missing:
                problems.append(f"{entry.get('id', '?')}: missing {missing}")
                continue
            for rel in (entry['cover'], entry['licenceFile']):
                if not os.path.exists(os.path.join(SHELF, rel)):
                    problems.append(f"{entry['id']}: {rel} does not exist")
            ext = os.path.splitext(entry['fileName'])[1].lower()
            if ext not in {'.gb', '.gbc', '.gba'}:
                problems.append(f"{entry['id']}: fileName must end in .gb/.gbc/.gba")
            if any('—' in str(v) or '–' in str(v) for v in entry.values() if isinstance(v, str)):
                problems.append(f"{entry['id']}: dash in text (house style: no em or en dashes)")

            local = local_path_for(entry['downloadURL'])
            if local:
                path = local
                if not os.path.exists(path):
                    problems.append(f"{entry['id']}: mirrored file {path} is missing")
                    continue
            else:
                path = os.path.join(tmp, entry['id'] + ext)
                try:
                    fetch(entry['downloadURL'], path)
                except Exception as e:  # noqa: BLE001
                    problems.append(f"{entry['id']}: download failed: {e}")
                    continue
            size = os.path.getsize(path)
            digest = sha256(path)
            if not header_ok(path, entry['system']):
                problems.append(f"{entry['id']}: file does not look like a {entry['system']} ROM")
            if verify:
                old = existing.get(entry['id'])
                if old and (old['sha256'] != digest or old['size'] != size):
                    problems.append(f"{entry['id']}: upstream file changed (sha {old['sha256'][:12]} -> {digest[:12]})")
            record = dict(entry)
            record['sha256'] = digest
            record['size'] = size
            out.append(record)
            print(f"{entry['id']:28} {size:>10} {digest[:16]}  {'local' if local else 'remote'}")

    if problems:
        print('\nPROBLEMS:')
        for p in problems:
            print(' -', p)
        if not verify:
            print('\ncatalog.json NOT written')
            return 1
        return 1

    if not verify:
        catalog = {
            'version': 1,
            'updated': source.get('updated', ''),
            'titles': out,
        }
        with open(os.path.join(SHELF, 'catalog.json'), 'w', encoding='utf-8', newline='\n') as f:
            json.dump(catalog, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f"\nwrote catalog.json with {len(out)} titles")
    else:
        print(f"\nverified {len(out)} titles")
    return 0


if __name__ == '__main__':
    sys.exit(build(verify='--verify' in sys.argv))
