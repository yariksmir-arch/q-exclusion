"""Replay all admitted finite suites, preserving their separate counts."""

if not __debug__:
    raise RuntimeError('OPTIMIZED_PYTHON_NOT_SUPPORTED: run finite checks without -O, -OO or PYTHONOPTIMIZE')

from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[2]
    for name in (
        'control_pass_regression.py',
        'semantic_roles_check.py',
        'articulation_check.py',
        'question_definability_check.py',
        'incidence_bounds_check.py',
        'transport_scope_check.py',
    ):
        subprocess.run(
            [sys.executable, str(root / 'research/regression' / name)],
            cwd=root, check=True,
        )
    print('CANONICAL_FINITE_REPLAY_PASS (separate suites; general proofs not mechanized)')


if __name__ == '__main__':
    main()
