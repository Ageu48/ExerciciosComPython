from random import randint
from time import sleep


def sorteia():
    print(f'Os 5 valores sorteados para lista foram → ', end='')
    for valor in range(0, 5):
        randomiza = randint(1, 10)
        numeros.append(randomiza)
        print(randomiza, end=' ')
        sleep(0.4)
    print('← PRONTO!',end='')


def somapar():
    soma_vlor = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma_vlor += valor
    print(f'\nA soma dos valores pares de {numeros}, temos → {soma_vlor}')


numeros = []
sorteia()
somapar()
