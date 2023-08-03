#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador-1': randint(1, 6),
        'jogador-2': randint(1, 6),
        'jogador-3': randint(1, 6),
        'jogador-4': randint(1, 6),}
ranking = []
for k, v in jogo.items():
    print(f'{k} tirou → \033[31m{v}\033[m no dado')
    sleep(0.5)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print('-=' * 30)
print(f'{"  == RANKING DOS JOGADORES ==  "}')
sleep(1)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar → {v[0]} com {v[1]}.')
