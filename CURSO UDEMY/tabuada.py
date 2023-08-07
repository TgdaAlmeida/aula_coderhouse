numero = int(input('Deseja a taboada de qual numero? '))


for i in range (1,11):
    produto = numero * i
    print (f'{numero} x {i} = {produto}')

