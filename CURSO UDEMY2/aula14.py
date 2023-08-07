#FORMATAÇAO

a = 'A'
b = 'B'
c = 1

string = 'b={nome1} a={nome0} a={nome1} c{nome2}'
formato = string.format(nome0=a, nome1=b, nome2=c)

print(formato)
