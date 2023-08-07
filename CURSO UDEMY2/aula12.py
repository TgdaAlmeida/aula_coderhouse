nome = 'Thiago Almeida'
altura = 1.82
peso = 93
imc = peso / (altura * altura)

#fstrings
info = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC e de {imc:.2f}'


print( nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC e', imc)
# ou
print(info)