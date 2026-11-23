# Roteiro para montar um modelo com a pessoa

Fale simples, um passo de cada vez, e explique cada termo na primeira vez que ele aparecer.

1. **Objetivo.** O que o modelo precisa responder? Quem vai ler?
2. **Tabelas principais.** Comece pelos assuntos centrais (cliente, pedido, produto). Detalhe depois.
3. **Grão.** Para cada tabela: o que uma linha representa? Escreva na descrição. Uma tabela não deve misturar grãos.
4. **Colunas.** Nome em `snake_case`, tipo e uma descrição que qualquer pessoa entenda.
5. **Chaves.** PK identifica a linha; FK aponta para a PK de outra tabela.
6. **Relacionamentos.** Arraste de coluna para coluna e confira a cardinalidade (`1` → `0..N` é o caso mais comum).
7. **Camadas.** `bronze` guarda o dado como chegou; `silver` limpa, tipa e deduplica; `gold` organiza para consumo (`dim` e `fact`).
8. **Áreas e notas.** Uma área por camada ou domínio. Dúvidas viram nota, nunca suposição.
9. **Validação.** Resolva os alertas e leia o board como alguém que nunca o viu.
10. **Exportação.** DDL para criar estruturas, `StructType` para PySpark, Mermaid para documentação, JSON para guardar ou mover o board.

Modelo dimensional em uma frase: a **fato** guarda os eventos e números (vendas, valores); as **dimensões** descrevem quem, o quê, quando e onde, e se ligam à fato por chaves substitutas (`sk_`).

Use exemplos fictícios. O app documenta a estrutura; não executa consultas nem mostra resultados de JOIN.
