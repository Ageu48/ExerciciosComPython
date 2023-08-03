from time import sleep
distancia = float(input('Qual a distancia da sua viagem? '))
print('Calculando valor da passagem para uma viagem de {:.2F}Km'.format(distancia))
sleep(3)
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('Valor da passagem será R$ {:.2F}'.format(preco))
