from random import randint
from time import sleep
print('{:=^40}'.format('JOKENPO')) #Aqui lembre disso
opções = ('PEDRA', 'PAPEL', 'TESOURA')
computador_escolha = randint(0,2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
usuario_escolha = int((input('Qual é a sua jogada? ')))
if usuario_escolha >= 3 or usuario_escolha < 0:
    print('JOGADA INVALIDA')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 14)
print('O computador escolheu {}'.format(opções[computador_escolha])) #Aqui lembre disso
print('Você escolheu {}'.format(opções[usuario_escolha])) #Aqui lembre disso
print('-=' * 14)
if computador_escolha == 0:
    if usuario_escolha == 0:
        print('EMPATE')
    elif usuario_escolha == 1:
        print('VITORIA')
    else:
        print('DERROTA')

elif computador_escolha == 1:
    if usuario_escolha == 0:
        print('DERROTA')
    elif usuario_escolha == 1:
        print('EMPATE')
    else:
        print('VITORIA')

elif computador_escolha == 2:
    if usuario_escolha == 0:
        print('VITORIA')
    elif usuario_escolha == 1:
        print('DERROTA')
    else:
        print('EMPATE')
