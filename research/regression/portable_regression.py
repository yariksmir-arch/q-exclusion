"""Run every stdlib Python suite. The separate 178-check PowerShell suite is not replaced."""

if not __debug__:
    raise RuntimeError('OPTIMIZED_PYTHON_NOT_SUPPORTED: run finite checks without -O, -OO or PYTHONOPTIMIZE')

from pathlib import Path
import subprocess
import sys

def main():
    root = Path(__file__).resolve().parents[2]
    names = ('control_deterministic_check.py', 'control_branching_check.py',
             'control_continuation_check.py', 'control_protocol_composition.py',
             'semantic_roles_check.py', 'articulation_check.py',
             'question_definability_check.py', 'incidence_bounds_check.py',
             'semantic_transition_check.py', 'transport_scope_check.py')
    for name in names:
        subprocess.run([sys.executable, '-B', str(root / 'research/regression' / name)],
                       cwd=root, check=True)
    for name in ('endogenous_check.py', 'interface_check.py', 'coordination_check.py',
                 'interface_question_check.py'):
        subprocess.run([sys.executable, '-B', str(root / 'research/verification' / name)],
                       cwd=root, check=True)
    print('PYTHON_FINITE_REPLAY_PASS (separate counts; excludes PowerShell 178 checks)')

if __name__ == '__main__':
    main()
