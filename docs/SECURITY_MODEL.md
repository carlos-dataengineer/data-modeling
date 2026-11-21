# Segurança e privacidade

O Data Modeling trabalha principalmente com a estrutura dos dados que a pessoa desenha. Mesmo sem guardar os registros de uma tabela, um modelo pode mostrar nomes de tabelas, colunas, regras de negócio e detalhes da arquitetura. Por isso, os arquivos do projeto e as exportações precisam ser tratados com cuidado.

## Cuidados no uso

- Use nomes e estruturas fictícias em exemplos públicos.
- Não coloque senhas, tokens, chaves de API ou strings de conexão no quadro.
- Não inclua dados pessoais ou informações de clientes.
- Antes de compartilhar um JSON, revise tabelas, colunas, notas e descrições.
- Não use o repositório público para guardar informações internas da empresa.

## Modo local

Quando o HTML é aberto diretamente no navegador, sem o ambiente hospedeiro compatível, o quadro funciona localmente e não tem armazenamento compartilhado nem salvamento automático garantido. Exporte o JSON para guardar uma cópia e proteja esse arquivo como qualquer documento que descreve uma arquitetura.

## Modo integrado

A aplicação reconhece um ambiente hospedeiro por meio de `window.claude`. Nesse modo, os dados, a identidade, as permissões e os recursos de colaboração dependem dos serviços e das configurações desse ambiente.

O código também inclui criptografia AES-GCM por meio da Web Crypto API e mecanismos de concessão e revogação de acesso. Isso é uma camada de proteção, mas não garante segurança completa por si só. O host, o banco, as permissões, a identidade e a gestão das chaves precisam estar configurados corretamente.

## Ao contribuir

Não envie dados reais, credenciais ou informações confidenciais em commits, issues, exemplos ou capturas de tela. Se encontrar um problema de segurança, siga as orientações do arquivo `SECURITY.md` em vez de publicar detalhes sensíveis em uma issue aberta.
