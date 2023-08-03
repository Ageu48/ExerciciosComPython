from random import randint
vitoria = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    tipo = ' '
    total = computador + jogador
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
    print(f'O computador joga {computador} e o jogador {jogador} o total é {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if total % 2 == 0:
        if tipo == 'P':
            print('Jogador vence!')
            vitoria += 1
        else:
            print('O computador venceu!')
            break
    elif total % 2 != 0:
        if tipo == 'I':
            print('Jogador vence!')
            vitoria += 1
        else:
            print('O coputador venceu!')
            break
print(f'GAME OVER!, Você venceu {vitoria} vezes')
