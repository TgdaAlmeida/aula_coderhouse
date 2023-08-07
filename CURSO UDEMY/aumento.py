

salario = float(input('Digite o salario da pessoa: '))

novo_salario = 0
porcentagem = 0

if salario <= 1000:
    novo_salario =+ (salario * 1.20)
    porcentagem = 20
elif salario <= 3000:
    novo_salario =+ (salario * 1.15)
    porcentagem = 15
elif salario <= 8000:
    novo_salario =+ (salario * 1.10)
    porcentagem = 10
else:
    novo_salario =+ (salario * 1.05)
    porcentagem = 5

aumento = (novo_salario - salario)


print(f'Novo salario: R$ {novo_salario:.2f}')
print(f'Aumento: R$ {aumento:.2f}')
print(f'Porcentagem: {porcentagem}%')



