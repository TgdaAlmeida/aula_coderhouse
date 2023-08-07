"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a #lista b passa a ter o msm valor da a, o valor nao e atribuido.
#passam ser a mesma coisa, mudou em uma, muda na outra.
lista_b = lista_a.copy() #copia os valores da lista a pra lista b

lista_a[0] = 'Qualquer coisa' #lista a alterada mas nao muda o valor da b, pois elas 
#nao sao mais vinculadas.
print(lista_a)
print(lista_b)