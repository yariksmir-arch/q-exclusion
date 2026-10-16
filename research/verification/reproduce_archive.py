"""Reproduce a byte-identical content ZIP from the verified public snapshot."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]

def main(output):
    output = Path(output).resolve()
    if not (not output.is_relative_to(ROOT)):
        raise ValueError('write the archive outside the snapshot')
    if not (not output.exists()):
        raise ValueError('refusing to overwrite an existing archive')
    subprocess.run([sys.executable, '-B', str(ROOT / 'research/verification/verify_public.py')], cwd=ROOT, check=True)
    manifest = json.loads((ROOT / 'MANIFEST.json').read_text(encoding='utf8'))
    paths = sorted([e['path'] for e in manifest['files']] + ['MANIFEST.json'])
    with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_STORED) as archive:
        for rel in paths:
            info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, (ROOT / rel).read_bytes())
    print(json.dumps({'archive': output.name, 'sha256': hashlib.sha256(output.read_bytes()).hexdigest(), 'entries': len(paths)}, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    main(parser.parse_args().output)
