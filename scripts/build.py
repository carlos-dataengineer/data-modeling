#!/usr/bin/env python3
"""Gera os arquivos distribuídos do Data Modeling a partir de src/data-modeling.html.

Entradas:
  src/data-modeling.html      fonte do app (fragmento, como o artefato do Claude espera)
  examples/loja-aurora.json   quadro de exemplo fictício embutido no app

Saídas:
  app/index.html                                        documento completo, abre direto no navegador
  skills/data-modeling/assets/data-modeling.html        cópia do documento completo (usada pela skill)
  skills/data-modeling/assets/data-modeling-artifact.html  fragmento para publicar como artefato no Claude
  skills/data-modeling/assets/loja-aurora.json          exemplo para importar

Uso:
  python scripts/build.py          gera os arquivos
  python scripts/build.py --check  falha se os arquivos gerados estiverem desatualizados
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "data-modeling.html"
DEMO = ROOT / "examples" / "loja-aurora.json"
PLACEHOLDER = "/*@@DEMO_BOARD@@*/null"

SKILL_ASSETS = ROOT / "skills" / "data-modeling" / "assets"
OUT_APP = ROOT / "app" / "index.html"
OUT_SKILL = SKILL_ASSETS / "data-modeling.html"
OUT_ARTIFACT = SKILL_ASSETS / "data-modeling-artifact.html"
OUT_DEMO = SKILL_ASSETS / "loja-aurora.json"

# Mesmo invólucro que o Claude usa ao baixar um artefato: estilos base e nada mais.
HEAD = (
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    "<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}"
    "body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}"
    "img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n"
)
TAIL = "</body></html>\n"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def build() -> dict[Path, str]:
    src = read(SRC)
    if src.count(PLACEHOLDER) != 1:
        raise SystemExit(f"Marcador {PLACEHOLDER} não encontrado (ou repetido) em {SRC}")
    demo_text = read(DEMO)
    demo = json.loads(demo_text)
    # JSON compacto; "</" escapado para não fechar a tag <script> por acidente.
    inline = json.dumps(demo, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    fragment = src.replace(PLACEHOLDER, inline).rstrip() + "\n"
    full = HEAD + fragment + TAIL
    return {OUT_APP: full, OUT_SKILL: full, OUT_ARTIFACT: fragment, OUT_DEMO: demo_text}


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for path, content in build().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        if check:
            stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
            print(f"gerado: {path.relative_to(ROOT).as_posix()}")
    if stale:
        print("Arquivos desatualizados. Rode: python scripts/build.py")
        for s in stale:
            print(f"  - {s}")
        return 1
    if check:
        print("Arquivos gerados em dia.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
