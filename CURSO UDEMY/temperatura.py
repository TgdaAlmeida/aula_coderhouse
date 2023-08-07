

escala = str(input('Voce vai digitar a temperatura em qual escala? (C/F)? '))

temperatura = 0
celsius = 0
fahrenheit = 0

if escala == 'F':
    temperatura = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = (5/9 * (temperatura - 32))
    print(f'Temperatura equivalente em Celsius: {celsius:.2f}')
elif escala == 'C':
    temperatura = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (temperatura * 1.8) + 32
    print(f'Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}')
else:
    print('Digite apenas F ou C')


    
