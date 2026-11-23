#!/usr/bin/env python3
"""Validações estáticas do repositório (sem navegador).

Confere: manifesto da skill, manifestos do plugin, versão consistente, arquivos
gerados, exemplo fictício, instaladores (ASCII sem BOM no .ps1), imagens e links
do README e, opcionalmente, termos privados que não podem ir para o GitHub.

Termos privados: defina DATA_MODELING_PROIBIDOS="termo1,termo2" antes de rodar.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "data-modeling"
errors: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


# Skill
skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
check(bool(m), "SKILL.md sem frontmatter YAML")
if m:
    front = dict(re.findall(r"^(\w+):\s*(.+)$", m.group(1), re.M))
    check(front.get("name") == "data-modeling", "SKILL.md: name deve ser 'data-modeling'")
    desc = front.get("description", "")
    check(20 <= len(desc) <= 1024, "SKILL.md: description deve ter entre 20 e 1024 caracteres")
for ref in re.findall(r"`((?:assets|references)/[^`]+)`", skill):
    check((SKILL / ref).exists(), f"SKILL.md cita {ref}, que não existe")
check((SKILL / "agents" / "openai.yaml").exists(), "falta skills/data-modeling/agents/openai.yaml (Codex)")

# Plugin e versão
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
check(plugin.get("name") == "data-modeling", "plugin.json: name deve ser 'data-modeling'")
check(plugin.get("version") == version, f"plugin.json: versão {plugin.get('version')} difere de VERSION {version}")
entries = [p for p in market.get("plugins", []) if p.get("name") == "data-modeling"]
check(len(entries) == 1, "marketplace.json: precisa de uma entrada 'data-modeling'")
if entries:
    check(entries[0].get("version") == version, "marketplace.json: versão difere de VERSION")
check(f"[{version}]" in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), f"CHANGELOG.md sem a versão {version}")
check(f"version: {version}" in (ROOT / "CITATION.cff").read_text(encoding="utf-8"), "CITATION.cff com versão diferente")

# Exemplo fictício
demo = json.loads((ROOT / "examples/loja-aurora.json").read_text(encoding="utf-8"))
check(demo.get("format") == "schema-board", "exemplo: format deve ser 'schema-board'")
tids = {t["id"]: {c["id"] for c in t["columns"]} for t in demo["tables"]}
for r in demo.get("rels", []):
    for end in ("from", "to"):
        e = r[end]
        check(e["t"] in tids and e["c"] in tids.get(e["t"], set()), f"exemplo: relação {r['id']} aponta para coluna inexistente")
item_ids = {o["id"] for k in ("tables", "notes", "frames", "texts", "shapes") for o in demo.get(k, [])}
for lk in demo.get("links", []):
    check(lk["from"]["id"] in item_ids and lk["to"]["id"] in item_ids, f"exemplo: conector {lk['id']} aponta para item inexistente")

# Arquivos gerados
for rel in ["app/index.html", "skills/data-modeling/assets/data-modeling.html", "skills/data-modeling/assets/data-modeling-artifact.html"]:
    p = ROOT / rel
    check(p.exists(), f"{rel} não existe (rode python scripts/build.py)")
    if p.exists():
        html = p.read_text(encoding="utf-8")
        check("<title>Data Modeling — modelagem de dados</title>" in html, f"{rel} sem o título Data Modeling")
        check("@@DEMO_BOARD@@" not in html, f"{rel} sem o exemplo embutido")
        check("Loja Aurora" in html, f"{rel} sem o exemplo Loja Aurora")
        check("window.claude" in html, f"{rel} perdeu a integração com o Claude")
        check("Schema Board" not in html, f"{rel} ainda mostra o nome antigo")
artifact = (SKILL / "assets" / "data-modeling-artifact.html").read_text(encoding="utf-8")
check(not re.search(r"<!doctype|<html|<body", artifact, re.I), "data-modeling-artifact.html não pode ter doctype/html/body")

# Instaladores
for rel in ["install.ps1", "uninstall.ps1"]:
    raw = (ROOT / rel).read_bytes()
    check(not raw.startswith(b"\xef\xbb\xbf"), f"{rel} não pode ter BOM (quebra o irm | iex)")
    check(all(b < 128 for b in raw), f"{rel} precisa ser ASCII puro (Windows PowerShell 5.1)")
for rel in ["install.sh", "uninstall.sh"]:
    raw = (ROOT / rel).read_bytes()
    check(raw.startswith(b"#!/usr/bin/env bash"), f"{rel} sem shebang")
    check(b"\r\n" not in raw, f"{rel} precisa de quebras de linha LF")

# README: imagens e links
readme = (ROOT / "README.md").read_text(encoding="utf-8")
imgs = re.findall(r'src="(docs/images/[^"]+)"', readme) + re.findall(r"!\[[^\]]*\]\((docs/images/[^)]+)\)", readme)
check(len(imgs) >= 8, "README deveria mostrar as capturas de tela")
for img in imgs:
    check((ROOT / img).exists(), f"README cita {img}, que não existe")
for md in [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]:
    text = md.read_text(encoding="utf-8")
    for link in re.findall(r"\]\(((?!https?://|#|mailto:)[^)\s]+)\)", text):
        target = (md.parent / link.split("#")[0]).resolve()
        check(target.exists(), f"{md.relative_to(ROOT).as_posix()} aponta para {link}, que não existe")

# Termos privados (opcional)
proibidos = [t.strip().lower() for t in os.environ.get("DATA_MODELING_PROIBIDOS", "").split(",") if t.strip()]
if proibidos:
    for p in ROOT.rglob("*"):
        if ".git" in p.parts or not p.is_file() or p.suffix.lower() in {".png", ".jpg", ".ico"}:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore").lower()
        for t in proibidos:
            check(t not in text, f"termo privado em {p.relative_to(ROOT).as_posix()}")

if errors:
    print("Falhas:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("Repositório válido.")
