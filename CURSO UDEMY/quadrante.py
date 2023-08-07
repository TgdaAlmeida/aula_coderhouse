print('Digite as coodenadas X e Y: ')
x = int(input())
y = int(input())
localizaçao = ''

while True:
    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        localizaçao = 'Quadrante 1'
    elif x < 0 and y > 0:
        localizaçao = 'Quadrante 2'
    elif x < 0 and y < 0:
        localizaçao = 'Quadrante 3'
    else:
        localizaçao = 'Quadrante 4'
     
        
        print(localizaçao)

    print('Digite as coodenadas X e Y: ')
    x = int(input())
    y = int(input())