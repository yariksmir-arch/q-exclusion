"""Read-only snapshot, link and dependency checks; stdlib only, no Git history needed."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import ast
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def payload_files():
    out = []
    for p in ROOT.rglob('*'):
        rel = p.relative_to(ROOT)
        if '.git' in rel.parts:
            continue
        if not (not p.is_symlink()):
            raise ValueError(('symlink', str(rel)))
        if p.is_file():
            out.append(rel.as_posix())
    return sorted(out)

def anchors(text):
    out, counts = set(), {}
    for line in text.splitlines():
        m = re.match(r'^#{1,6}\s+(.*?)(?:\s+#+)?$', line)
        if m:
            slug = re.sub(r'[^\w\-\s]', '', m[1].lower()).replace(' ', '-')
            n = counts.get(slug, 0)
            counts[slug] = n + 1
            out.add(slug + ('-' + str(n) if n else ''))
    out.update(re.findall(r'(?:id|name)=["\x27]([^"\x27]+)', text))
    return out

def links(text):
    clean, fence = [], None
    for line in text.splitlines():
        m = re.match(r'^\s*(' + chr(96) + r'{3,}|~{3,})', line)
        if m:
            fence = None if fence == m[1][0] else m[1][0] if fence is None else fence
        elif fence is None:
            clean.append(line)
    text = '\n'.join(clean)
    yield from (m[1].strip('<>') for m in re.finditer(r'!?\[[^\]\n]*\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)', text))
    yield from (m[1].strip('<>') for m in re.finditer(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', text, re.M))

def main(require_approved=False, require_licensed=False):
    manifest = json.loads((ROOT / 'MANIFEST.json').read_text(encoding='utf8'))
    if not (manifest['schema_version'] == 2):
        raise ValueError('unsupported manifest schema')
    entries = manifest['files']
    expected = {e['path'] for e in entries}
    if not (len(expected) == len(entries)):
        raise ValueError('duplicate manifest paths')
    actual = set(payload_files())
    if not (actual == expected | {'MANIFEST.json'}):
        raise ValueError(('file set', sorted(actual - expected - {'MANIFEST.json'}), sorted(expected - actual)))
    internal_links = 0
    python_files = 0
    for e in entries:
        rel = e['path']
        p = (ROOT / rel).resolve()
        if not (p.is_relative_to(ROOT) and not Path(rel).is_absolute()):
            raise ValueError(rel)
        data = p.read_bytes()
        if not (digest(data) == e['sha256'] and len(data) == e['bytes']):
            raise ValueError(('hash', rel))
        expected_license = ('License-text-own-terms' if rel == 'LICENSES/CC-BY-4.0.txt' else
                            'MIT' if p.suffix in ('.py', '.ps1', '.yml') or rel in ('.gitattributes', '.gitignore', 'LICENSE') else 'CC-BY-4.0')
        if not (e['license'] == expected_license):
            raise ValueError(('licence coverage', rel))
        if p.suffix == '.md':
            text = data.decode('utf8')
            for dest in links(text):
                u = urlsplit(dest)
                if u.scheme or dest.startswith('//'):
                    if not (u.scheme in ('https', 'http', 'mailto')):
                        raise ValueError((rel, dest))
                    continue
                target = ((ROOT / unquote(u.path).lstrip('/')) if dest.startswith('/') else (p.parent / unquote(u.path))) if u.path else p
                if not (target.resolve().is_relative_to(ROOT) and target.is_file()):
                    raise ValueError(('link', rel, dest))
                if u.fragment and target.suffix == '.md':
                    if not (unquote(u.fragment).lower() in anchors(target.read_text(encoding='utf8'))):
                        raise ValueError(('anchor', rel, dest))
                internal_links += 1
        if p.suffix == '.py':
            tree = ast.parse(data.decode('utf8'), filename=rel)
            python_files += 1
            for node in ast.walk(tree):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module] if isinstance(node, ast.ImportFrom) and node.module else []
                for name in names:
                    first = name.split('.')[0]
                    if not (first in sys.stdlib_module_names or (p.parent / (first + '.py')).is_file()):
                        raise ValueError(('non-stdlib dependency', rel, first))
    for path, expected_hash in manifest['frozen_sha256'].items():
        if not (digest((ROOT / path).read_bytes()) == expected_hash):
            raise ValueError(('normative bytes', path))
    if not (not (ROOT / '.gitmodules').exists()):
        raise ValueError('submodules forbidden')
    approval = json.loads((ROOT / 'LICENSE-STATUS.json').read_text(encoding='utf8'))
    if manifest['licensing_status'] == 'ACTIVE' or require_licensed or require_approved:
        if not (approval['schema_version'] == 2 and approval['owner_approved'] and approval['owner_statement']):
            raise ValueError('LICENSE_APPROVAL_REQUIRED')
        if not (approval['code_license'] == 'MIT' and approval['text_and_metadata_license'] == 'CC-BY-4.0'):
            raise ValueError('LICENSE_SCOPE_MISMATCH')
        if not (approval['copyright_year'] == 2026 and approval['copyright_holder'] == 'Yaroslav Vyacheslavovich Smirnov'):
            raise ValueError('COPYRIGHT_NOTICE_MISMATCH')
        if not (manifest['licensing_status'] == 'ACTIVE' and manifest['manifest_license'] == 'CC-BY-4.0'):
            raise ValueError('LICENSES_NOT_ACTIVE')
        if not (manifest['release_authorized'] == approval['release_authorized']):
            raise ValueError('RELEASE_STATUS_MISMATCH')
        if not (manifest['publication_and_push_authorized'] == approval['publication_and_push_authorized']):
            raise ValueError('PUBLICATION_STATUS_MISMATCH')
        for e in entries:
            if e['license'] == 'License-text-own-terms':
                if not (e['copyright_holder'] is None and e['copyright_year'] is None):
                    raise ValueError('THIRD_PARTY_TEXT_RELICENSED')
            else:
                if not (e['copyright_holder'] == approval['copyright_holder'] and e['copyright_year'] == approval['copyright_year']):
                    raise ValueError(('copyright coverage', e['path']))
        mit = (ROOT / 'LICENSE').read_text(encoding='utf8')
        content = (ROOT / 'LICENSE-CONTENT.md').read_text(encoding='utf8')
        notice = (ROOT / 'NOTICE.md').read_text(encoding='utf8')
        if not ('Copyright © 2026 ' + approval['copyright_holder'] in mit and 'Permission is hereby granted' in mit):
            raise ValueError('MIT_GRANT_MISSING')
        if not ('are licensed under the Creative Commons Attribution 4.0 International license (CC BY 4.0).' in content):
            raise ValueError('CONTENT_GRANT_MISSING')
        if not (approval['copyright_holder'] in content and approval['copyright_holder_native'] in notice):
            raise ValueError('ATTRIBUTION_MISSING')
        if not (not (ROOT / 'LICENSES/MIT.proposed.txt').exists() and not (ROOT / 'NOTICE').exists()):
            raise ValueError('OBSOLETE_DRAFT_NOTICE_INCLUDED')
    if require_approved:
        if not (approval['release_authorized'] and approval['publication_and_push_authorized']):
            raise ValueError('PUBLICATION_NOT_AUTHORIZED')
    print(json.dumps({'status': 'PUBLIC_SNAPSHOT_PASS', 'payload_files': len(actual),
                      'local_links': internal_links, 'python_sources': python_files,
                      'frozen_bytes_unchanged': True, 'third_party_runtime_packages': 0,
                      'owner_approved': approval['owner_approved'],
                      'licensing_status': manifest['licensing_status'],
                      'release_authorized': approval['release_authorized'],
                      'publication_and_push_authorized': approval['publication_and_push_authorized'],
                      'general_proofs_mechanized': False}, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--require-licensed', action='store_true', help='require effective owner-approved licence grants')
    parser.add_argument('--require-approved', action='store_true', help='also require authorization for Codex publication/push actions')
    args = parser.parse_args()
    main(args.require_approved, args.require_licensed)
