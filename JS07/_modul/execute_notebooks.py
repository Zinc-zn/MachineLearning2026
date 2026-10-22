# -*- coding: utf-8 -*-
"""Eksekusi notebook JS07 dengan kernel venv lokal."""
import os
import sys

import nbformat
from nbclient import NotebookClient

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS = sys.argv[1:] or [
    "JS07_01.ipynb", "JS07_02.ipynb", "JS07_03.ipynb", "JS07_Tugas.ipynb",
]

for name in NOTEBOOKS:
    path = os.path.join(BASE, name)
    print(f"== executing {name} ==", flush=True)
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=3600, kernel_name="python3",
                            resources={"metadata": {"path": BASE}})
    try:
        client.execute()
        nbformat.write(nb, path)
        print("   OK", flush=True)
    except Exception as e:
        nbformat.write(nb, path)  # simpan state output sampai cell yang gagal
        print(f"   FAILED: {e}", flush=True)
        sys.exit(1)
