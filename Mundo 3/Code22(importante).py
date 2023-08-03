jogador = dict()
gol_partida = []
cont = 0
jogador['Nome'] = str(input('Nome do joagdor: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for p in range(partidas):
    gol_partida.append(int(input(f'Quantos gols na partida {p+1}? ')))
jogador['Gols'] = gol_partida[:]
jogador['Total de gols'] = sum(gol_partida)
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'na partida → {i+1}, fez → {v} gols.')
print(f'Foi um total de {sum(jogador["Gols"])} gols.')
