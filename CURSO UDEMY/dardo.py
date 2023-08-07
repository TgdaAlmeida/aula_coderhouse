
print('Digite as tres distancias: ')
d1 = input('')
d2 = input('')
d3 = input('')
maior_distancia = ''


if d1 > d2 and d1 > d3:
    maior_distancia = d1
elif d2 > d3 and d2 > d1:
    maior_distancia = d2
else:
    maior_distancia = d3

print(f'Maior distancia: {maior_distancia}')