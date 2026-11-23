# O que já está pronto e o que quero melhorar

Este documento separa os recursos que já existem das ideias que ainda quero desenvolver. Uma ideia no roadmap não deve ser entendida como uma função disponível.

## Já está disponível

- [x] Aplicação visual para desenhar tabelas e colunas.
- [x] Definição de tipos, descrições, PK e FK.
- [x] Relacionamentos e cardinalidades.
- [x] Organização por camadas, áreas, notas, textos, formas e conectores.
- [x] Busca, zoom, minimapa, grade, seleção, desfazer e refazer.
- [x] Importação de DDL e JSON.
- [x] Exportação SQL DDL Databricks/Delta, PySpark `StructType`, Mermaid ER e JSON.
- [x] Skill para orientar um agente de IA a instalar e usar a ferramenta.
- [x] Documentação de uso, arquitetura, privacidade e limites.
- [x] Instalação com um comando para Claude Code e Codex (v2.0.0).
- [x] Salvamento local no navegador e exemplo fictício Loja Aurora embutido (v2.0.0).
- [x] Referência visual dos controles e atalhos no README (v2.0.0).
- [x] Teste de fumaça no navegador e validação do repositório no CI (v2.0.0).

## Melhorias que quero avaliar

- [ ] Ampliar os testes de importação, exportação e validação.
- [ ] Melhorar a acessibilidade e a experiência em telas menores.

## Ideias para trabalhar com JOINs e transformações

- [ ] Criar um construtor visual para montar uma sequência de JOINs.
- [ ] Permitir escolher INNER, LEFT, RIGHT e FULL OUTER JOIN.
- [ ] Definir as condições de relacionamento entre as tabelas.
- [ ] Mostrar uma prévia usando conjuntos de dados pequenos e fictícios.
- [ ] Exibir quantidade de linhas antes e depois e alertar sobre possíveis duplicações.
- [ ] Gerar SQL `SELECT` para documentar ou implementar transformações.

## Ideias para linhagem e documentação

- [ ] Representar tabelas de origem e tabelas derivadas.
- [ ] Mostrar a linhagem entre colunas e transformações.
- [ ] Registrar o grão e as regras de negócio de cada tabela.
- [ ] Gerar documentação técnica mais completa.
- [ ] Avaliar integrações opcionais com plataformas de dados, sem armazenar credenciais no projeto.

## Como vou considerar uma melhoria pronta

Uma ideia só deve sair desta lista quando estiver implementada, testada e documentada. Até lá, ela continua sendo uma possibilidade para uma versão futura.
