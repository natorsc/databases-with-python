#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CRUD - pyodbc - Microsoft Access."""

import pathlib
import pyodbc

BASE_DIR = pathlib.Path(__file__).resolve().parent
DB_FILE = BASE_DIR.joinpath('exemplo.accdb')

con = pyodbc.connect(
            'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            # Deve ser utilizado o path/caminho absoluto até o arquivo.
            f'DBQ={DB_FILE};'
        )

cur = con.cursor()

     