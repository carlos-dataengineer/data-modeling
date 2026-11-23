---
name: data-modeling
description: Abre o Data Modeling, um quadro visual para desenhar e documentar modelos de dados (tabelas, colunas, tipos, PK/FK, relacionamentos com cardinalidade, camadas bronze/silver/gold, áreas, notas, formas e conectores) e exportar SQL DDL Databricks/Delta, PySpark StructType, Mermaid ER e JSON. Use quando a pessoa pedir "data modeling", "/data-modeling", "schema board", um diagrama ER, um modelo de dados, um quadro de tabelas, uma modelagem dimensional (fato e dimensões) ou a arquitetura medalhão de um pipeline. Use também para entregar um modelo já desenhado a partir de um CREATE TABLE ou de uma descrição.
---

# Data Modeling

O Data Modeling é uma ferramenta pronta, em um único arquivo HTML. **Nunca reescreva a ferramenta de memória e nunca gere uma versão "parecida"**: use sempre os arquivos da pasta `assets/` ao lado deste `SKILL.md`, sem alterar o código.

| Arquivo | Para quê |
|---|---|
| `assets/data-modeling-artifact.html` | Publicar como artefato no Claude (ferramenta Artifact). Fragmento sem `<html>`/`<body>`, como o artefato exige. |
| `assets/data-modeling.html` | Documento completo. Abrir no navegador (Codex, terminal) ou colar como artefato HTML no claude.ai. |
| `assets/loja-aurora.json` | Quadro de exemplo fictício (Loja Aurora), no formato JSON do app. |
| `references/FORMATO-JSON.md` | Formato do JSON, para entregar um modelo já desenhado. |
| `references/GUIA-MODELAGEM.md` | Roteiro para ajudar a pessoa a montar um bom modelo. |

## 1. Escolha como entregar

Siga a primeira opção que o ambiente permitir.

**A. Claude com a ferramenta Artifact** (Claude Code no app desktop, claude.ai com artefatos publicados)

1. Antes de criar outro, liste os artefatos da pessoa (`action: "list"`). Se já existir um chamado **Data Modeling**, ofereça abrir esse (`action: "open"`) em vez de duplicar: cada artefato guarda os próprios boards.
2. Para criar: publique `assets/data-modeling-artifact.html` com `icon: "database"`, a descrição "Quadro visual de modelagem de dados" e estas capacidades (o app já foi escrito para elas):
   `capabilities: {"db": {}, "user": {"scopes": ["profile"]}, "room": {}, "downloads": true}`
   - `db` guarda os boards (criptografados no próprio app), `user` identifica quem é dono e mostra nomes, `room` mostra quem está no board ao vivo e `downloads` entrega os arquivos exportados.
   - Se a ferramenta pedir um passo de design, o arquivo já está pronto: não mude o visual.
3. Entregue o link e explique: no primeiro acesso a pessoa cria um board em **Novo board**; o botão **Carregar exemplo** traz o modelo fictício Loja Aurora.

**B. claude.ai sem a ferramenta Artifact** (chat com artefatos HTML)

Crie um artefato do tipo HTML cujo conteúdo é **exatamente** o arquivo `assets/data-modeling.html`, sem resumir nem cortar. Nesse caso ele roda em modo local.

**C. Codex, Claude Code no terminal ou qualquer agente sem artefatos**

1. Se `~/DataModeling/data-modeling.html` já existir (o instalador cria), use-o. Senão, copie `assets/data-modeling.html` para lá. Crie a pasta se faltar e não sobrescreva um arquivo diferente sem perguntar.
2. Abra no navegador padrão:
   - Windows: `Start-Process "$HOME\DataModeling\data-modeling.html"`
   - macOS: `open ~/DataModeling/data-modeling.html`
   - Linux: `xdg-open ~/DataModeling/data-modeling.html`
3. Diga o caminho do arquivo. Em modo local o board fica salvo no navegador; para guardar uma cópia, **Exportar → JSON**.

## 2. Modelo já desenhado (opcional)

Quando a pessoa pedir um modelo pronto ("modele meu pipeline de vendas", "transforme este CREATE TABLE em diagrama"):

- **Tem DDL?** Não converta à mão: abra o app e oriente **Importar → SQL DDL** (ou colar o `CREATE TABLE` direto no canvas). O app entende Databricks, Spark SQL, Oracle e Postgres, inclusive `COMMENT`, `NOT NULL`, `PRIMARY KEY` e `FOREIGN KEY`.
- **Só uma descrição?** Monte o JSON seguindo `references/FORMATO-JSON.md` (use `assets/loja-aurora.json` como modelo) e:
  - **modo local (opção B ou C):** faça uma cópia de `assets/data-modeling.html` e insira, logo antes do último `<script>` do arquivo, a linha `<script>window.DATA_MODELING_BOARD = { ... };</script>` (escreva cada `<` dentro do JSON como `<`). Não altere mais nada. O app abre com o modelo e o salva no navegador com uma chave própria.
  - **artefato (opção A):** os boards ficam no banco do artefato. Entregue o JSON para a pessoa colar em **Importar → JSON do Data Modeling**.

Use nomes e dados fictícios em exemplos. Nunca coloque credenciais, dados pessoais ou amostras reais no quadro.

## 3. Depois de entregar

Explique em poucas linhas:

- Ferramentas na barra da esquerda, com atalhos: `T` tabela, `N` nota, `X` texto, `S` forma, `L` conector, `F` área, `V` selecionar, `H` mover o canvas. Duplo clique no fundo cria uma tabela.
- Para ligar tabelas, arraste a bolinha ao lado de uma coluna até a coluna de destino. Soltar no cabeçalho de outra tabela cria a FK `id_<tabela>`.
- O painel da direita edita nome, camada, schema, colunas (tipo, PK, FK, NOT NULL, descrição) e cardinalidade.
- **Validação** (canto inferior) aponta tabela sem PK, FK sem relação, tipos diferentes numa junção.
- **Exportar**: SQL DDL Databricks/Delta, PySpark `StructType`, Mermaid ER e JSON. O DDL define estruturas; não é consulta nem transformação.
- `?` mostra todos os atalhos. `Ctrl+K` busca, `Shift+1` enquadra tudo, `Ctrl+Z` desfaz.

Para ajudar a pensar o modelo (grão, chaves, camadas), siga `references/GUIA-MODELAGEM.md`. Não prometa recursos que o app não tem: ele não executa SQL, não conecta ao Databricks e não mostra prévia de JOINs.
