print(f'{" MATRIZ 3 X 3 ":=^40}')
matriz = [[0,0,0,], [0,0,0], [0,0,0]]
somaPar = somaTerceira = maiorVlor = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a MATRIZ [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
print('===' * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'As somas dos valores pares é → {somaPar}')
for linha in range(0, 3):
    somaTerceira += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaTerceira}')
for coluna in range(0, 3):
    if coluna == 0:
        maiorVlor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorVlor:
        maiorVlor = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorVlor}')
