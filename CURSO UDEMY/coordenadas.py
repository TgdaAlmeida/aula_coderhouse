valorX = float(input('Valor de X: '))
valorY = float(input('Valor de Y: '))

localizaçao = ''

if valorX > 0 and valorY > 0:
    localizaçao = 'Q1'
elif valorX < 0 and valorY >= 0:
    localizaçao = 'Q2'
elif valorX < 0 and valorY <0:
    localizaçao = 'Q3'
elif valorX == 0 and valorY == 0:
    localizaçao = 'Origem'
elif valorX == 0:
    localizaçao = 'Eixo Y'
elif valorY == 0:
    localizaçao = 'Eixo X' 
else:
    localizaçao = 'Q4'

print(localizaçao)


