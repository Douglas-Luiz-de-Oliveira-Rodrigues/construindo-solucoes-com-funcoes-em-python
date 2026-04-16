
n = int(input())

acervo = {}

for _ in range(n):
    linha = input().strip()
    partes = linha.split()
    codigo = partes[-1]
    titulo = ' '.join(partes[:-1])
    acervo[titulo] = codigo

consulta = input().strip()

if consulta in acervo:
    print(acervo[consulta])
else:
    print("Livro nao encontrado")