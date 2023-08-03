from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = cont = 0
print('Os valores sorteados foram: ', end='')
for t in tupla:
    print(f'{t} ', end='')
    cont += 1
    if cont == 1:
        maior = t
        menor = t
    if t > maior:
        maior = t
    if t < menor:
        menor = t
print(f'\nMAIOR valor é {maior}')
print(f'MENOR valor é {menor}')
