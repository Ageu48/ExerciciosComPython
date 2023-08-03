from random import randint
from time import sleep
print('---' * 15)
print(f'{"JOGA NA MEGA SENA":^40}')
print('---' * 15)
tot = 1
lista = [] #lista temporaria que vai armazenar os valores randomizados
jogos = [] #lista que armazena a lista acima ja randomizada
escolha = int(input('Quantos jogos quer sortear? '))
while tot <= escolha:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])   #copia a lista
    lista.clear()  #limpa a lista para sortear novos valores
    tot += 1
print('-=' * 6, f'SORTEANDO {escolha} JOGOS', '-=' * 6)
for i, l in enumerate(jogos):
    print(f'Jogos {i + 1}: {l}')
    sleep(1)
print('-=' * 6, '< BOA SORTE! > ', '-=' * 6)
