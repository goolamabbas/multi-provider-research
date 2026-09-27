#!/usr/bin/env python3
"""Build the installable skill ZIP from tracked files, without repository extras."""
import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
skill = root / 'skills/multi-provider-research'
version = re.search(r'^  version: "([0-9]+\.[0-9]+\.[0-9]+)"$',
                    (skill / 'SKILL.md').read_text(), re.M).group(1)
tracked = subprocess.check_output(['git', 'ls-files', '-z', 'skills/multi-provider-research'], cwd=root).decode().split('\0')
files = [(root / p, 'multi-provider-research/' + Path(p).relative_to('skills/multi-provider-research').as_posix()) for p in tracked if p]
files.append((root / 'LICENSE', 'multi-provider-research/LICENSE'))
args.output.mkdir(parents=True, exist_ok=True)
archive = args.output / f'multi-provider-research-v{version}.zip'
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for source, name in sorted(files, key=lambda item: item[1]):
        if source.is_symlink():
            raise ValueError(f'Unexpected symlink: {source}')
        entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        z.writestr(entry, source.read_bytes())
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
(args.output / 'SHA256SUMS').write_text(f'{digest}  {archive.name}\n')
print(f'{archive}: {len(files)} files; SHA-256 {digest}')
