codigo = float(input('Codigo do produto comprado: '))
quantidade_comprada = float(input('Quantidade comprada: '))
pagar = 0


if codigo == 1:
    pagar = (5.00 * quantidade_comprada)
elif codigo == 2:
    pagar = (3.50 * quantidade_comprada)
elif codigo == 3:
    pagar = (4.80 * quantidade_comprada)
elif codigo == 4:
    pagar = (8.90 * quantidade_comprada)
elif codigo == 5:
    pagar = (7.32 * quantidade_comprada)
else:
    print('Digite um codigo valido.')

print(f'Valor a pagar: R$ {pagar:.2f}')
  

    


