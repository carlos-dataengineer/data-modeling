---
name: data-modeling
description: Ajuda a instalar e usar o Data Modeling para desenhar e documentar tabelas, colunas, chaves, relacionamentos e camadas de dados. Orienta a revisão e a exportação para SQL DDL Databricks/Delta, PySpark StructType, Mermaid ER e JSON.
license: Apache-2.0
compatibility: Requer Python 3.9+ para executar o instalador. A aplicação precisa de um navegador moderno. Recursos de colaboração dependem de um ambiente hospedeiro compatível com window.claude.
metadata:
  author: krlos
  version: "1.0.5"
---

# Data Modeling

## Para que serve

Use esta Skill quando alguém quiser instalar, abrir, entender ou trabalhar com o Data Modeling.

O Data Modeling é um quadro visual para desenhar estruturas de dados. Ele ajuda a mostrar quais tabelas existem, quais colunas fazem parte delas, como as tabelas se relacionam e em quais camadas estão organizadas.

O aplicativo incluído em `Assets/index.html` é a aplicação visual do Data Modeling. Preserve o comportamento real do arquivo. Não substitua a ferramenta por uma versão simplificada sem autorização.

## Como chamar a Skill

Depois de copiar a pasta `data-modeling` para o diretório de Skills do agente, abra uma nova sessão. No Claude Code, use `/data-modeling`. No Codex, selecione a Skill pelo menu `/skills` ou invoque `$data-modeling`, conforme a versão do host.

## Como instalar

Execute o instalador:

```bash
python <skill-root>/Scripts/install.py --target ./data-modeling
```

Ele cria `index.html`, `sample-project.json` e `README.md` na pasta indicada. Não diga que a instalação terminou sem executar o script e conferir os arquivos. A instalação não abre o aplicativo automaticamente.

## Como ajudar alguém a montar um modelo

1. Entenda o que a pessoa quer representar.
2. Liste as tabelas principais.
3. Para cada tabela, defina o grão: o que uma linha representa?
4. Adicione colunas, tipos e descrições.
5. Marque as chaves primárias (PK) e estrangeiras (FK).
6. Desenhe os relacionamentos e confira a cardinalidade.
7. Organize as tabelas nas camadas disponíveis: `raw`, `bronze`, `silver`, `gold`, `stage`, `dim`, `fact` e entidade.
8. Use áreas, notas, textos, formas e conectores para explicar o desenho.
9. Execute a validação e revise os alertas.
10. Exporte o formato adequado para o próximo passo.

Explique os termos técnicos quando aparecerem. Por exemplo, PK é a chave que identifica um registro; FK é a chave que aponta para outra tabela; cardinalidade mostra quantos registros podem se relacionar.

## Recursos existentes

- Quadro visual com tabelas e colunas.
- Tipos de dados, descrições, PK e FK.
- Relacionamentos e cardinalidades.
- Camadas, áreas, notas, textos, formas e conectores.
- Validação, busca, minimapa, zoom, grade, seleção, desfazer e refazer.
- Importação de DDL e JSON.
- Exportação SQL DDL Databricks/Delta, PySpark `StructType`, Mermaid ER e JSON.

Recursos de colaboração, presença, sincronização e controle de acesso dependem do ambiente hospedeiro que fornece `window.claude` e os serviços necessários.

## Como escolher a exportação

- **DDL:** para documentar a definição das estruturas das tabelas.
- **PySpark `StructType`:** para representar os campos e tipos no código PySpark.
- **Mermaid ER:** para incluir o diagrama em documentação compatível.
- **JSON:** para guardar ou transportar o quadro e importá-lo novamente.

O DDL é uma definição de estrutura. Não é um `SELECT`, não executa consultas e não realiza transformações.

## Limites que devem ser explicados

Esta versão não executa JOINs sobre registros, não mostra prévia de linhas resultantes, não cria tabelas derivadas, não executa SQL ou pipelines e não se conecta diretamente ao Databricks. Construtor de JOINs, prévia de resultados e linhagem são ideias futuras, não recursos atuais.

## Modos de execução

- **Com ambiente hospedeiro compatível:** o aplicativo pode usar os serviços de banco, usuário, sala, presença, sincronização e downloads disponibilizados pelo host.
- **Sem esse ambiente:** abre em modo local, sem armazenamento compartilhado e sem garantia de salvamento automático. Oriente a pessoa a exportar o JSON para guardar uma cópia.

## Privacidade

Use nomes, identificadores, organizações e estruturas fictícias em exemplos públicos. Não inclua dados pessoais, dados de clientes, credenciais, tokens, senhas, URLs internas ou amostras reais. Um JSON exportado pode conter nomes de tabelas, colunas, descrições e decisões de arquitetura; recomende revisar o arquivo antes de compartilhar.

## Como explicar a ferramenta

Fale de forma simples e prática. Comece com um exemplo pequeno, explique o grão, as chaves e os relacionamentos e só depois apresente as exportações. Nunca prometa recursos que não existem no HTML atual.
