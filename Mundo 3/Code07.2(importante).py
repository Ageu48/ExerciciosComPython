lista_valores = []
maior = menor = 0
for posicao in range(0, 5):
    lista_valores.append(int(input(f'Digite um valor para posição {posicao}: ')))
    if posicao == 0:
        maior = menor = lista_valores[posicao]
    if lista_valores[posicao] > maior:
        maior = lista_valores[posicao]
    if lista_valores[posicao] < menor:
        menor = lista_valores[posicao]
print('--' * 20)
print(f'Os valores digitados foram → {lista_valores}')
print(f'O MAIOR valor da lista é → {maior} e ele esta na posição → ', end='')
for indice, valor in enumerate(lista_valores):
    if valor == maior:
        print(f'{indice}...', end='')
print(f'\nO menor valor da lista é → {menor} e ele esta na posição → ', end='')
for indice, valor in enumerate(lista_valores):
    if valor == menor:
        print(f'{indice}...', end='')
