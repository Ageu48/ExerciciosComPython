from random import randint
vitoria = 0
while True:
    computador = randint(0, 10)
    escolha = str(input('Escolha [PAR/IMPAR]: ')).strip()[0]
    jogador = int(input('Escolha um numero: '))
    resultado = (jogador + computador) % 2
    if resultado == 0 and escolha in 'pP':
        vitoria += 1
        print(f'O computador jogou {computador} e o jogador {jogador}, se \033[33m{computador + jogador} é PAR\033[m')
        print('\033[32mJogador vencê\033[m')
    if resultado == 0 and escolha in 'iI':
        print(f'O computador escolheu {computador} e o jogador {jogador}, se \033[31m{computador + jogador} é PAR\033[m')
        print('\033[31mJogador perde\033[m')
        break
    if resultado != 0 and escolha in 'iI':
        vitoria += 1
        print(f'O computador jogou {computador} e o jogador {jogador}, se \033[33m{computador + jogador} é IMPAR\033[m')
        print('\033[32mJogador vencê\033[m')
    if resultado != 0 and escolha in 'pP':
        print(f'O computador escolheu {computador} e o jogador {jogador}, se \033[31m{computador + jogador} é IMPAR\033[m')
        print('\033[31mJogador perde\033[m')
        break
print('~~~~' * 14)
print(f'Com um total de \033[32m{vitoria}\033[m VITORIAS consecutivas')
print('~~~~' * 14)
