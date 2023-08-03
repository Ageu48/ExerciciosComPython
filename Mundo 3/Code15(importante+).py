#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-86-matriz-em-python/
print(f'{" MATRIZ 3 X 3 ":=^40}')
matriz = [[0,0,0,], [0,0,0], [0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a MATRIZ [{linha}, {coluna}]: '))
print('===' * 15)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
