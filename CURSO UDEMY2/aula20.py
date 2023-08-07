#EXERCICO IF ELIF ELSE 

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f"primeiro_valor = '{primeiro_valor}' e maior que o segundo_valor = '{segundo_valor}'")
else:
    print(f"segundo_valor = '{segundo_valor}' e maior que o primeiro_valor = '{primeiro_valor}'")

