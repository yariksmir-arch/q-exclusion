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
        assert not p.is_symlink(), ('symlink', str(rel))
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
    assert manifest['schema_version'] == 2, 'unsupported manifest schema'
    entries = manifest['files']
    expected = {e['path'] for e in entries}
    assert len(expected) == len(entries), 'duplicate manifest paths'
    actual = set(payload_files())
    assert actual == expected | {'MANIFEST.json'}, ('file set', sorted(actual - expected - {'MANIFEST.json'}), sorted(expected - actual))
    internal_links = 0
    python_files = 0
    for e in entries:
        rel = e['path']
        p = (ROOT / rel).resolve()
        assert p.is_relative_to(ROOT) and not Path(rel).is_absolute(), rel
        data = p.read_bytes()
        assert digest(data) == e['sha256'] and len(data) == e['bytes'], ('hash', rel)
        expected_license = ('License-text-own-terms' if rel == 'LICENSES/CC-BY-4.0.txt' else
                            'MIT' if p.suffix in ('.py', '.ps1', '.yml') or rel in ('.gitattributes', '.gitignore', 'LICENSE') else 'CC-BY-4.0')
        assert e['license'] == expected_license, ('licence coverage', rel)
        if p.suffix == '.md':
            text = data.decode('utf8')
            for dest in links(text):
                u = urlsplit(dest)
                if u.scheme or dest.startswith('//'):
                    assert u.scheme in ('https', 'http', 'mailto'), (rel, dest)
                    continue
                target = ((ROOT / unquote(u.path).lstrip('/')) if dest.startswith('/') else (p.parent / unquote(u.path))) if u.path else p
                assert target.resolve().is_relative_to(ROOT) and target.is_file(), ('link', rel, dest)
                if u.fragment and target.suffix == '.md':
                    assert unquote(u.fragment).lower() in anchors(target.read_text(encoding='utf8')), ('anchor', rel, dest)
                internal_links += 1
        if p.suffix == '.py':
            tree = ast.parse(data.decode('utf8'), filename=rel)
            python_files += 1
            for node in ast.walk(tree):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module] if isinstance(node, ast.ImportFrom) and node.module else []
                for name in names:
                    first = name.split('.')[0]
                    assert first in sys.stdlib_module_names or (p.parent / (first + '.py')).is_file(), ('non-stdlib dependency', rel, first)
    for path, expected_hash in manifest['frozen_sha256'].items():
        assert digest((ROOT / path).read_bytes()) == expected_hash, ('normative bytes', path)
    assert not (ROOT / '.gitmodules').exists(), 'submodules forbidden'
    approval = json.loads((ROOT / 'LICENSE-STATUS.json').read_text(encoding='utf8'))
    if manifest['licensing_status'] == 'ACTIVE' or require_licensed or require_approved:
        assert approval['schema_version'] == 2 and approval['owner_approved'] and approval['owner_statement'], 'LICENSE_APPROVAL_REQUIRED'
        assert approval['code_license'] == 'MIT' and approval['text_and_metadata_license'] == 'CC-BY-4.0', 'LICENSE_SCOPE_MISMATCH'
        assert approval['copyright_year'] == 2026 and approval['copyright_holder'] == 'Yaroslav Vyacheslavovich Smirnov', 'COPYRIGHT_NOTICE_MISMATCH'
        assert manifest['licensing_status'] == 'ACTIVE' and manifest['manifest_license'] == 'CC-BY-4.0', 'LICENSES_NOT_ACTIVE'
        assert manifest['release_authorized'] == approval['release_authorized'], 'RELEASE_STATUS_MISMATCH'
        assert manifest['publication_and_push_authorized'] == approval['publication_and_push_authorized'], 'PUBLICATION_STATUS_MISMATCH'
        for e in entries:
            if e['license'] == 'License-text-own-terms':
                assert e['copyright_holder'] is None and e['copyright_year'] is None, 'THIRD_PARTY_TEXT_RELICENSED'
            else:
                assert e['copyright_holder'] == approval['copyright_holder'] and e['copyright_year'] == approval['copyright_year'], ('copyright coverage', e['path'])
        mit = (ROOT / 'LICENSE').read_text(encoding='utf8')
        content = (ROOT / 'LICENSE-CONTENT.md').read_text(encoding='utf8')
        notice = (ROOT / 'NOTICE.md').read_text(encoding='utf8')
        assert 'Copyright (c) 2026 ' + approval['copyright_holder'] in mit and 'Permission is hereby granted' in mit, 'MIT_GRANT_MISSING'
        assert 'are licensed under the Creative Commons Attribution 4.0 International license (CC BY 4.0).' in content, 'CONTENT_GRANT_MISSING'
        assert approval['copyright_holder'] in content and approval['copyright_holder_native'] in notice, 'ATTRIBUTION_MISSING'
        assert not (ROOT / 'LICENSES/MIT.proposed.txt').exists() and not (ROOT / 'NOTICE').exists(), 'OBSOLETE_DRAFT_NOTICE_INCLUDED'
    if require_approved:
        assert approval['release_authorized'] and approval['publication_and_push_authorized'], 'PUBLICATION_NOT_AUTHORIZED'
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
