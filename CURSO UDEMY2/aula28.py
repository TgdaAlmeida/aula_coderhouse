"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} ok
        Seu nome invertido é {nome invertido} ok
        Seu nome contém (ou não) espaços ok
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra} ok
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome contem espacos.')
    else:
        print(f'Seu nome NAO contem espaços.')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
    
else:
    print(f'Desculpe, voce deixou campos vazios.')


