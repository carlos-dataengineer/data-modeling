# Formato JSON do Data Modeling

É o mesmo JSON de **Exportar → JSON** e de **Importar → JSON do Data Modeling**. O campo `format` continua `"schema-board"` por compatibilidade com boards antigos. Exemplo completo: `../assets/loja-aurora.json`.

```json
{
  "format": "schema-board",
  "version": 1,
  "board": { "name": "Loja Aurora · vendas (exemplo)", "catalog": "aurora_dev" },
  "tables": [], "rels": [], "notes": [], "frames": [], "texts": [], "shapes": [], "links": []
}
```

Só `tables` é obrigatório. Coordenadas em pixels do canvas (`x` para a direita, `y` para baixo); podem ser negativas.

## tables

| Campo | Tipo | Observação |
|---|---|---|
| `id` | string | único no arquivo, ex.: `t_pedido` |
| `name` | string | `snake_case` |
| `layer` | string | `raw`, `bronze`, `silver`, `gold`, `stage`, `dim`, `fact` ou `other` (entidade) |
| `schema`, `catalog` | string | formam o nome completo `catalog.schema.name` no DDL; `catalog` vazio usa o do board |
| `desc` | string | o que uma linha representa (o grão) |
| `x`, `y`, `w` | número | posição e largura (padrão 400; 340 fica bom) |
| `collapsed` | boolean | opcional, mostra só o cabeçalho |
| `columns` | lista | ver abaixo |

Altura de uma tabela: `38 + 26 × número de colunas`. Deixe uns 60 px entre tabelas.

Coluna: `{ "id": "c_id_pedido", "name": "id_pedido", "type": "bigint", "pk": true, "fk": false, "nn": true, "desc": "Chave do pedido" }`. Tipos comuns: `string`, `bigint`, `int`, `decimal(12,2)`, `date`, `timestamp`, `boolean`. O `id` da coluna precisa ser único dentro da tabela.

## rels (relacionamentos entre colunas)

```json
{ "id": "r1", "from": { "t": "t_cliente", "c": "c_id_cliente" }, "to": { "t": "t_pedido", "c": "c_id_cliente" },
  "fromCard": "1", "toCard": "0..N", "label": "faz" }
```

`from` aponta para o lado da PK; `to` para a FK. Cardinalidades: `1`, `0..1`, `1..N`, `0..N`.

## Itens de apoio

- `frames` (áreas): `{ "id", "x", "y", "w", "h", "title", "color": "#B98F12" }`
- `notes` (post-its): `{ "id", "x", "y", "w", "text", "color": "y|b|g|p|o" }`
- `texts` (títulos): `{ "id", "x", "y", "text", "size": 48, "bold": true, "color": "ink|muted|accent|hot|ok" }`
- `shapes`: `{ "id", "type": "rect|pill|ellipse|diamond|cylinder|para", "x", "y", "w", "h", "text", "color": "accent|ok|warn|hot|err", "fs": 16 }`
- `links` (conectores entre quaisquer itens): `{ "id", "from": { "kind": "shape", "id": "s1" }, "to": { "kind": "table", "id": "t_x" }, "style": "solid|dashed", "arrow": "end", "color": "edge", "label": "" }` — `kind` pode ser `table`, `note`, `text`, `shape` ou `frame`.

Antes de entregar, confira: todo `rels.from/to` e `links.from/to` aponta para um `id` existente, e não há dados reais.
