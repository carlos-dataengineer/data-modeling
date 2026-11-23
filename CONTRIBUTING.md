# Como contribuir

1. Abra uma issue descrevendo problema, contexto e comportamento esperado.
2. Para mudanças maiores, discuta a proposta antes de implementar.
3. Crie uma branch curta a partir de `main`.
4. Mantenha a aplicação standalone e evite dependências externas sem justificativa.
5. Use somente dados fictícios em testes, screenshots e exemplos.
6. Edite só `src/data-modeling.html` e `examples/loja-aurora.json`; rode `python scripts/build.py`, `python tests/validate_repo.py` e `python tests/test_smoke.py` (detalhes em [docs/DESENVOLVIMENTO.md](docs/DESENVOLVIMENTO.md)).
7. Atualize documentação e `CHANGELOG.md`.
8. Abra um pull request com resumo, motivação, testes e screenshots quando houver mudança visual.

## Padrões
- HTML/CSS/JS legíveis e sem dependências runtime desnecessárias.
- Nomes em `snake_case` nos modelos de dados.
- Mensagens e documentação em português brasileiro; nomes técnicos podem permanecer em inglês.
- Não inclua segredos ou dados reais nos commits.
