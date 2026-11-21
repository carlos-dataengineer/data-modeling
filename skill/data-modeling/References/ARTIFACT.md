# Sobre o aplicativo

`Assets/index.html` é a aplicação visual do Data Modeling. Ela reúne tabelas, colunas, chaves, relacionamentos, camadas e elementos de apoio em um quadro.

O aplicativo pode ser aberto em um navegador moderno. Sem um ambiente hospedeiro compatível com `window.claude`, funciona em modo local, sem armazenamento compartilhado e sem salvamento automático garantido.

As exportações disponíveis são SQL DDL Databricks/Delta, PySpark `StructType`, Mermaid ER e JSON. O SQL gerado define estruturas; não é uma consulta de transformação. Esta versão não executa JOINs nem gera tabelas resultantes.
