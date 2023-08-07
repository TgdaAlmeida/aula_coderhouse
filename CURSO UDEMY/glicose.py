
glicose = float(input('Digite a medida de glicose: '))

print('Classificaçao: ', end='')

if glicose <= 100:
    print('Normal')
elif glicose <= 140:
    print('Elevado')
else:
    print('Diabetes')
