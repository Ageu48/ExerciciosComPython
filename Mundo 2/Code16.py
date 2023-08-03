from random import randint
computador = randint(0, 10)
jogador = int(input('Pensei em um numero entre 0 e 10. Tente adivinhar: '))
palpite = 1
while jogador != computador:
    palpite += 1
    if jogador > computador:
        jogador = int(input('Menos... Tente novamente: '))
    elif jogador < computador:
        jogador = int(input('Mais... Tente novamente: '))
print('O computador pensou em {} e o jogador em {}, Você acertou. '.format(computador, jogador))
print('\033[32mVocê precisou de {} tentativas. PARABENS!!'.format(palpite))
