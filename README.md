# Desafio Clientes Exclusivos: Filtrando Dados Sem Duplicidade

## Desafio de Código

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
[Link para o desafio]()
