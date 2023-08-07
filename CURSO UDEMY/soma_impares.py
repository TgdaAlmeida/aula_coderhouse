

print('Digite 2 numeros:')
x = int(input())
y = int(input())

posicao = 0
soma = 0

if x > y:
    troca = x
    x = y
    y = troca


for i in range(x+1,y):
    if i % 2 != 0:
        soma = i + soma
print(f'SOMA DOS IMPARES: {soma}')
    
