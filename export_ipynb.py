# /// script
# requires-python = ">=3.11"
# dependencies = ["nbformat"]
# ///
"""
Export notebook.py to notebook.ipynb, with outputs, for GitHub

The interactive section is left out, because its controls do not work
in a static notebook. The sections after it are renumbered.
"""

import re
import subprocess
import sys

import nbformat

SKIP = "Interactive"

subprocess.run(
    [
        sys.executable, "-m", "marimo", "export", "ipynb", "notebook.py",
        "-o", "notebook.ipynb", "--include-outputs", "--sort", "top-down", "-f",
    ],
    check=True,
)

nb = nbformat.read("notebook.ipynb", as_version=4)
cells = []
skipping = False
number = 0
for cell in nb.cells:
    if cell.cell_type == "markdown" and (
        m := re.match(r"## \d+\. (.*)", cell.source)
    ):
        skipping = m.group(1).startswith(SKIP)
        if not skipping:
            number += 1
            cell.source = re.sub(r"## \d+\.", f"## {number}.", cell.source, count=1)
    if not skipping:
        cells.append(cell)
nb.cells = cells
nbformat.write(nb, "notebook.ipynb")
