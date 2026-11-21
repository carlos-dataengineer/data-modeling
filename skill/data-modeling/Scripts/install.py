#!/usr/bin/env python3
"""Materialize the Data Modeling browser application from this skill package."""
from __future__ import annotations
import argparse
import json
import shutil
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser(description="Install the Data Modeling browser artifact.")
    parser.add_argument("--target", required=True, help="Directory where Data Modeling will be created.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    app = root / "Assets" / "index.html"
    sample = root / "Assets" / "sample-project.json"
    if not app.is_file() or not sample.is_file():
        parser.error("Skill package is incomplete: Assets/index.html or sample-project.json is missing.")
    target = Path(args.target).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(app, target / "index.html")
    shutil.copy2(sample, target / "sample-project.json")
    (target / "README.md").write_text(
        "# Data Modeling\n\n"
        "Abra `index.html` em um navegador moderno. O arquivo `sample-project.json` é um exemplo fictício. "
        "Sem um ambiente hospedeiro compatível com `window.claude`, o quadro funciona em memória, "
        "sem armazenamento compartilhado e sem salvamento automático garantido. Exporte o JSON "
        "pela aplicação para guardar uma cópia.\n",
        encoding="utf-8",
    )
    print(f"Data Modeling instalado em: {target}")
    print("Abra index.html no navegador. A colaboração remota depende do ambiente hospedeiro window.claude.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
