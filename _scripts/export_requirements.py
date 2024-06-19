# -*- coding: utf-8 -*-
"""Export requirements.txt."""

import pathlib
import subprocess

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent


def export_with_pdm() -> None:
    subprocess.call(
        args=['pdm', 'export', '--without-hashes', '-o', 'requirements.txt'],
        cwd=ROOT_DIR,
    )


def export_with_poetry() -> None:
    subprocess.call(
        args=[
            'poetry',
            'export',
            '--without-hashes',
            '-o',
            'requirements.txt',
        ],
        cwd=ROOT_DIR,
    )


if __name__ == '__main__':
    print('[!] Criando requirements [!]')
    # export_with_pdm()
    export_with_poetry()
    print('[!] Requirements criado [!]')
