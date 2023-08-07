#ENUNCIADOS

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero: ')


if numero.isdigit():
    inteiro = int(numero)
    par_impar = inteiro % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O numero {inteiro} e {par_impar_texto}')

else:
    print('Voce nao digitou um numero inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = int(input('Digite a hora em inteiro: '))


try:
    hora = int(entrada)

    if hora >=0 and hora <=11:
        print('Bom dia!')
    elif hora >=12 and hora <=17:
        print('Boa tarde!')
    elif hora >=18 and hora <=23:
        print('Boa noite!')
    else:
        print('Nao conheço essa hora!')

except:
    print('Por favor digite apenas numeros inteiros!')

#if entrada < 12:
#   print('Bom dia!')
#elif entrada <= 17:
#    print('Boa tarde!')
#else:
#   print('Boa noite!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')

letras = len(nome)

if letras > 1:
    if letras <= 4:
        print('Seu nome e curto!')
    elif letras <= 6:
        print('Seu nome e normal!')
    else:
        print('Seu nome e muito grande!')
else:
    print('Digite mais de uma letras')
