#!/usr/bin/env python3
"""Verify reviewed rule snapshots locally, optionally against their Raw URLs."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BASE = 'https://raw.githubusercontent.com/riddikuluswen/Rule/refs/heads/main/ClashMeta/'


def verify(entry, remote):
    data = (ROOT / entry['file']).read_bytes()
    assert len(data) == entry['bytes'], entry['file']
    assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['file']
    rules = [line for line in data.decode('utf-8').splitlines() if line and not line.startswith('#')]
    assert len(rules) == entry['rules'], entry['file']
    assert len(set(rules)) == len(rules), entry['file']
    assert all(line.split(',')[0] in {'DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD', 'DOMAIN-WILDCARD',
               'DOMAIN-REGEX', 'IP-CIDR', 'IP-CIDR6', 'AND', 'OR', 'NOT', 'DST-PORT', 'NETWORK'} for line in rules), entry['file']
    assert not any('//' in line or '#' in line for line in rules), entry['file']
    if remote:
        request = Request(BASE + entry['file'], headers={'User-Agent': 'Rule-snapshot-verifier'})
        with urlopen(request, timeout=60) as response:
            assert response.status == 200, entry['file']
            assert response.headers.get_content_type() in {'text/plain', 'application/octet-stream'}, entry['file']
            assert response.read() == data, entry['file']
    return entry['rules']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--remote', action='store_true', help='also download and compare every public Raw file')
    args = parser.parse_args()
    entries = json.loads((ROOT / 'manifest.json').read_text())['files']
    assert len({entry['file'] for entry in entries}) == len(entries)
    with ThreadPoolExecutor(max_workers=4) as pool:
        counts = list(pool.map(lambda entry: verify(entry, args.remote), entries))
    print(f'PASS: {len(counts)} rule sets, {sum(counts):,} rules; remote={args.remote}')


if __name__ == '__main__':
    main()
