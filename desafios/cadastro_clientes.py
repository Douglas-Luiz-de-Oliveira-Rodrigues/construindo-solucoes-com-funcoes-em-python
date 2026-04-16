def formatar_nome(nome):
    return ' '.join(palavra.capitalize() for palavra in nome.strip().split())

def validar_email(email):
    if email.count('@') != 1:
        return False
    
    partes = email.split('@')
    parte_apos_arroba = partes[1]
    
    if '.' not in parte_apos_arroba:
        return False
    
    return True

def processar_cadastro(entrada):
    if ', ' not in entrada:
        return 'Entrada inválida - ERRO'
    
    nome, email = entrada.split(', ', 1)
    nome_formatado = formatar_nome(nome)
    
    if validar_email(email):
        return f"{nome_formatado} - OK"
    else:
        return f"{nome_formatado} - ERRO"

entrada = input()
print(processar_cadastro(entrada))