# Desafio de Código: Construindo Soluções com Funções em Python

## Clientes Exclusivos: Filtrando Dados Sem Duplicidade

Você foi contratado por uma consultoria para organizar dados de clientes de diferentes projetos.  
Cada projeto fornece uma lista de nomes de clientes, mas há duplicatas e inconsistências entre os projetos.  
O objetivo é identificar rapidamente quais clientes são exclusivos de cada projeto, garantindo dados limpos e sem repetições desnecessárias.

### Regras de Negócio
- Receber duas listas de nomes de clientes (uma por linha).
- Identificar os nomes que aparecem **apenas em uma das listas**.
- Exibir os nomes exclusivos em **ordem alfabética**.
- Se não houver nomes exclusivos, imprimir **"Nenhum"**.
- Não utilizar bibliotecas externas.

### Entrada
Duas linhas contendo listas de nomes separados por espaço.  
As listas podem estar vazias.

### Saída
Uma linha com os nomes exclusivos de cada projeto, separados por espaço e em ordem alfabética.  
Se não houver nomes exclusivos, exibir **"Nenhum"**.

### Exemplos
| Entrada                        | Saída                |
|--------------------------------|----------------------|
| ana bruno carla<br>carla diego | ana bruno diego      |
| lucas maria<br>lucas maria     | Nenhum               |
| joao<br>                       | joao                 |
| paula rafa<br>                 | paula rafa           |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica
- **Conjuntos (set)**: para eliminar duplicatas e comparar listas
- **Manipulação de strings**: divisão e ordenação de nomes
- **Estruturas condicionais**: para decidir se há nomes exclusivos ou não

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio](https://github.com/Douglas-Luiz-de-Oliveira-Rodrigues/construindo-solucoes-com-funcoes-em-python/blob/main/desafios/clientes_exclusivos.py)

---

## Busca Eficiente de Livros em Acervo Digital com Dicionários

Você foi contratado por uma biblioteca digital que deseja organizar seu acervo de livros de forma eficiente.  
Cada livro é identificado por um título e um código único. Para facilitar buscas rápidas, os dados são armazenados em um **dicionário**, onde a chave é o título e o valor é o código correspondente.  
Sua tarefa é implementar um programa que encontre o código de um livro a partir do seu título.

### Regras de Negócio
- Ler um número inteiro `N`, indicando a quantidade de livros cadastrados.
- Ler `N` linhas, cada uma contendo um título e um código separados por espaço.
- Ler o título a ser consultado.
- Se o título existir no acervo → imprimir o código correspondente.
- Caso contrário → imprimir **"Livro nao encontrado"**.

### Entrada
- Primeira linha: número inteiro `N` (quantidade de livros).  
- Próximas `N` linhas: título e código separados por espaço.  
- Última linha: título do livro a ser consultado.

### Saída
- O código correspondente ao título consultado.  
- Ou a mensagem **"Livro nao encontrado"** se o título não existir.

### Exemplos
| Entrada                                                                  | Saída                |
|--------------------------------------------------------------------------|----------------------|
| 3<br>Python101 001<br>Algoritmos 002<br>Redes 003<br>Python101           | 001                  |
| 2<br>IntroJava 100<br>Estruturas 200<br>Estruturas                       | 200                  |
| 1<br>BancoDeDados 555<br>Redes                                           | Livro nao encontrado |
| 2<br>LivroA 10<br>LivroB 20<br>LivroC                                    | Livro nao encontrado |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica
- **Dicionários (`dict`)**: para armazenar pares título-código
- **Manipulação de strings**: leitura e separação de dados
- **Estruturas condicionais**: para verificar se o título existe no acervo

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio](https://github.com/Douglas-Luiz-de-Oliveira-Rodrigues/construindo-solucoes-com-funcoes-em-python/blob/main/desafios/busca_livros.py)

---

## Funções Reutilizáveis Para Cadastro de Clientes em Python

Você foi contratado por uma consultoria em TI para ajudar a organizar o sistema de cadastro de clientes.  
O objetivo é criar funções reutilizáveis que centralizem operações como padronizar nomes e validar e-mails, facilitando futuras manutenções e evitando erros.

### Regras de Negócio
- Receber uma linha contendo **nome completo** e **e-mail**, separados por vírgula e espaço.
- Validar o e-mail:
  - Deve conter **exatamente um '@'**
  - Deve conter pelo menos um **'.'** após o '@'
- Padronizar o nome:
  - Primeira letra de cada palavra em maiúsculo
  - Demais letras em minúsculo
- Exibir:
  - `Nome Formatado - OK` se o e-mail for válido
  - `Nome Formatado - ERRO` caso contrário

### Entrada
Uma única linha contendo o nome completo e o e-mail, separados por vírgula e espaço.

### Saída
Uma única linha com o nome formatado, seguido de `- OK` ou `- ERRO`.

### Exemplos
| Entrada                          | Saída              |
|----------------------------------|--------------------|
| ana silva, ana.silva@email.com   | Ana Silva - OK     |
| joao, joao@email                 | Joao - ERRO        |
| maria clara, maria@email.com     | Maria Clara - OK   |
| carlos, carlos@@email.com        | Carlos - ERRO      |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica
- **Funções reutilizáveis**: para validação de e-mail e formatação de nome
- **Manipulação de strings**: `split`, `title`, `strip`
- **Estruturas condicionais**: para verificar validade do e-mail

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio](https://github.com/Douglas-Luiz-de-Oliveira-Rodrigues/construindo-solucoes-com-funcoes-em-python/blob/main/desafios/cadastro_clientes.py)
