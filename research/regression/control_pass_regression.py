"""One entry point for the preserved baseline and this optional control pass."""
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[2]
    subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass',
                    '-File', str(root / 'research/regression/finite_regression.ps1')],
                   cwd=root, check=True)
    for name in ('control_deterministic_check.py', 'control_branching_check.py',
                 'control_continuation_check.py', 'control_protocol_composition.py'):
        subprocess.run([sys.executable, str(root / 'research/regression' / name)],
                       cwd=root, check=True)
    print('CONTROL_PASS_REGRESSION_PASS (baseline and all four optional suites)')


if __name__ == '__main__':
    main()
