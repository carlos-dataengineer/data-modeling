#!/usr/bin/env python3
"""Teste de fumaça: abre o Data Modeling num navegador real e exercita o básico.

Requer: pip install playwright && python -m playwright install chromium
Uso:    python tests/test_smoke.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
APP = (ROOT / "app" / "index.html").as_uri()
DEMO = json.loads((ROOT / "examples" / "loja-aurora.json").read_text(encoding="utf-8"))
KEY = "data-modeling:local:v1"


def saved(page):
    page.wait_for_timeout(700)  # o salvamento local é adiado em 300 ms
    raw = page.evaluate(f"localStorage.getItem('{KEY}')")
    return json.loads(raw) if raw else None


def main() -> int:
    failures: list[str] = []
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception:
            browser = p.chromium.launch(channel="msedge")
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" and "fonts.g" not in m.text else None)

        # 1. Abre em modo local com o exemplo fictício
        page.goto(APP)
        page.wait_for_timeout(1200)
        if page.title() != "Data Modeling — modelagem de dados":
            failures.append(f"título inesperado: {page.title()!r}")
        n = page.locator("#tables > *").count()
        if n != len(DEMO["tables"]):
            failures.append(f"esperava {len(DEMO['tables'])} tabelas do exemplo, vi {n}")
        if "Loja Aurora" not in page.locator("#boardName").inner_text():
            failures.append("o nome do board de exemplo não apareceu")
        if "Salvo no navegador" not in page.locator("#sync").inner_text():
            failures.append("o indicador de modo local não diz 'Salvo no navegador'")

        # 2. Cria uma tabela (T + clique) e confere o salvamento local
        page.keyboard.press("t")
        page.mouse.click(700, 820)
        page.keyboard.press("Escape")
        snap = saved(page)
        if not snap or len(snap["tables"]) != len(DEMO["tables"]) + 1:
            failures.append("a tabela nova não foi salva no navegador")

        # 3. Recarrega: o board continua lá
        page.reload()
        page.wait_for_timeout(1200)
        if page.locator("#tables > *").count() != len(DEMO["tables"]) + 1:
            failures.append("depois de recarregar, a tabela nova sumiu")

        # 4. Exporta DDL com o catálogo fictício
        page.locator("#exportBtn").click()
        ddl = page.locator("#xcode").input_value()
        if "CREATE TABLE" not in ddl or "aurora_dev.gold.fato_vendas" not in ddl:
            failures.append("o DDL exportado não tem aurora_dev.gold.fato_vendas")
        page.locator('[data-xtab="mmd"]').click()
        if "erDiagram" not in page.locator("#xcode").input_value():
            failures.append("a exportação Mermaid não gerou erDiagram")
        page.locator('[data-xtab="py"]').click()
        if "StructType" not in page.locator("#xcode").input_value():
            failures.append("a exportação PySpark não gerou StructType")
        if page.locator("#modalRoot [data-close]").count():
            page.locator("#modalRoot [data-close]").first.click()

        # 5. Importa um CREATE TABLE
        page.locator("#importBtn").click()
        page.locator("#icode").fill(
            "CREATE TABLE aurora_dev.silver.tb_cupom (\n  id_cupom BIGINT NOT NULL COMMENT 'Cupom',\n"
            "  codigo STRING,\n  CONSTRAINT pk_tb_cupom PRIMARY KEY (id_cupom)\n) USING DELTA;"
        )
        page.locator("[data-iok]").click()
        snap = saved(page)
        if not snap or not any(t["name"] == "tb_cupom" for t in snap["tables"]):
            failures.append("o CREATE TABLE importado não virou tabela")

        # 6. Validação aponta os alertas didáticos do exemplo
        page.locator("#lintBtn").click()
        page.wait_for_timeout(300)
        lint = page.locator("#lintPanel").inner_text() if page.locator("#lintPanel").is_visible() else "(painel fechado)"
        if "em validação" not in lint or "sem fonte" not in lint:
            failures.append("a validação não mostrou os alertas do exemplo: " + lint[:120])

        # 7. Board vazio oferece 'Carregar exemplo'
        page.evaluate(f"localStorage.setItem('{KEY}', JSON.stringify({{format:'schema-board',version:1,board:{{name:'Vazio'}},tables:[]}}))")
        page.reload()
        page.wait_for_timeout(1000)
        btn = page.locator('#empty [data-act="load-demo"]')
        if not btn.count():
            failures.append("o board vazio não oferece 'Carregar exemplo'")
        else:
            btn.click()
            page.wait_for_timeout(500)
            if page.locator("#tables > *").count() != len(DEMO["tables"]):
                failures.append("'Carregar exemplo' não trouxe as tabelas do exemplo")

        if errors:
            failures.append("erros no console: " + " | ".join(errors[:5]))
        browser.close()

    if failures:
        print("Falhas:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("Teste de fumaça ok.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
