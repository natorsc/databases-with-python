# -*- coding: utf-8 -*-
"""."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent


def make_requirements(shell: bool = False):
    subprocess.call(
        args=['poetry', 'export', '--without-hashes',
              '-f', 'requirements.txt', '-o', 'requirements.txt'],
        cwd=ROOT_DIR,
        shell=shell,
    )


def make_requirements_dev(shell: bool = False):
    subprocess.call(
        args=['poetry', 'export', '--with', 'dev', '--without-hashes',
              '-f', 'requirements.txt', '-o', 'requirements-dev.txt'],
        cwd=ROOT_DIR,
        shell=shell,
    )


if __name__ == "__main__":
    import platform

    system = platform.system()
    if system == 'Windows':
        make_requirements(shell=True)
        make_requirements_dev(shell=True)
    else:
        make_requirements()
        make_requirements_dev()
