#!/usr/bin/env python3
"""Gera as capturas de tela do README em docs/images/ a partir de app/index.html.

Usa só o exemplo fictício Loja Aurora que vem embutido no app.

Requer: pip install playwright && python -m playwright install chromium
Uso:    python scripts/screenshots.py
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Page, sync_playwright

ROOT = Path(__file__).resolve().parent.parent
APP = (ROOT / "app" / "index.html").as_uri()
OUT = ROOT / "docs" / "images"
W, H = 1600, 900


def fresh(browser, width=W, height=H, mobile=False) -> Page:
    ctx = browser.new_context(viewport={"width": width, "height": height}, device_scale_factor=1,
                              is_mobile=mobile, has_touch=mobile)
    page = ctx.new_page()
    page.goto(APP)
    page.wait_for_timeout(1500)  # fontes + enquadramento
    page.evaluate("document.fonts && document.fonts.ready")
    return page


def shot(page: Page, name: str) -> None:
    page.wait_for_timeout(350)
    page.screenshot(path=str(OUT / name))
    print("ok", name)


def table(page: Page, name: str):
    return page.locator("#tables .table").filter(has_text=name).first


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception:
            browser = p.chromium.launch(channel="msedge")

        # Visão geral (tema escuro, padrão)
        page = fresh(browser)
        shot(page, "visao-geral.png")

        # Tema claro
        page.locator("#themeBtn").click()
        shot(page, "tema-claro.png")
        page.locator("#themeBtn").click()

        # Tabela selecionada: painel de edição e junções destacadas
        table(page, "fato_vendas").locator(".t-head").click()
        shot(page, "tabela-selecionada.png")

        # Detalhe: zoom na silver para ler colunas, chaves e cardinalidades
        page.keyboard.press("Escape")
        page.mouse.move(520, 560)
        for _ in range(6):
            page.mouse.wheel(0, -120)
            page.wait_for_timeout(60)
        shot(page, "detalhe-silver.png")
        page.keyboard.press("Shift+1")

        # Seleção múltipla: alinhar, distribuir, agrupar
        page.mouse.click(W // 2, 860)
        page.keyboard.press("Control+a")
        shot(page, "selecao-multipla.png")
        page.keyboard.press("Escape")

        # Validação
        page.locator("#lintBtn").click()
        shot(page, "validacao.png")
        page.locator("#lintBtn").click()

        # Busca
        page.keyboard.press("Control+k")
        page.keyboard.type("cliente", delay=20)
        shot(page, "busca.png")
        page.keyboard.press("Escape")

        # Minimapa + grade
        page.locator("#miniBtn").click()
        page.locator("#gridBtn").click()
        shot(page, "minimapa.png")
        page.locator("#miniBtn").click()
        page.locator("#gridBtn").click()

        # Exportar: DDL, PySpark, Mermaid
        page.locator("#exportBtn").click()
        shot(page, "exportar-ddl.png")
        page.locator('[data-xtab="py"]').click()
        shot(page, "exportar-pyspark.png")
        page.locator('[data-xtab="mmd"]').click()
        shot(page, "exportar-mermaid.png")
        page.locator("#modalRoot [data-close]").first.click()

        # Importar DDL
        page.locator("#importBtn").click()
        page.locator("#icode").fill(
            "CREATE TABLE aurora_dev.silver.tb_cupom (\n"
            "  id_cupom BIGINT NOT NULL COMMENT 'Identificador do cupom',\n"
            "  codigo STRING COMMENT 'Código digitado no checkout',\n"
            "  pct_desconto DECIMAL(5,2),\n"
            "  dt_validade DATE,\n"
            "  CONSTRAINT pk_tb_cupom PRIMARY KEY (id_cupom)\n"
            ") USING DELTA;"
        )
        shot(page, "importar-ddl.png")
        page.locator("#modalRoot [data-close]").first.click()

        # Atalhos
        page.locator("#helpBtn").click()
        shot(page, "atalhos.png")
        page.locator("#modalRoot [data-close]").first.click()
        page.context.close()

        # Celular
        page = fresh(browser, 390, 844, mobile=True)
        shot(page, "celular.png")
        page.context.close()
        browser.close()


if __name__ == "__main__":
    main()
