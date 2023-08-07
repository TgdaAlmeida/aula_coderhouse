#EXERCICO WHILE

nome = 'Thiago Almeida'

tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)
print(nome[0])

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)