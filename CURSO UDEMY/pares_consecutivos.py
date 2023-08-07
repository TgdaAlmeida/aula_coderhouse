
#numero = int(input('Digite um inteiro: '))

#if (numero%2) == 0:
#    print("Par")
#else:
#    print("Ímpar")



numero = int(input('Digite um numero inteiro: '))

soma = 0
soma : int

while numero != 0:
    if (numero % 2) == 0:
        soma = numero + (numero + 2) + (numero + 4) + (numero + 6) + (numero + 8)
        print(soma)
    else:
        soma = (numero + 1) + (numero + 3) + (numero + 5) + (numero + 7) + (numero + 9)
        print(soma)
    numero = int(input('Digite um numero inteiro: '))
    

print('Fim!')



x = int(input("Digite um numero inteiro: "))

while x != 0:
	if x % 2 != 0:
		x = x + 1

	soma = 5 * x + 20
	print(f"SOMA = {soma}")

	x = int(input("Digite um numero inteiro: "))
