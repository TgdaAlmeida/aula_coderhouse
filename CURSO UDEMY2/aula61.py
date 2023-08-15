cpf = input('Digite o numero do CPF: ')
nove_digitos = cpf[:9]


resultado = 0
contador_regressivo_1 = 10

for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

print(resultado)

digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0
print(digito_1)

dez_digitos = cpf[:9] + str(digito_1)
resultado_2 = 0
contador_regressivo_2 = 11

for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

print(resultado_2)

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0
print(digito_2)