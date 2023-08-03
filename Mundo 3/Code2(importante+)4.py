list_jogadores = list()
cont = 0
while True:
    jogador = dict()
    gols = list()
    jogador['nome'] = str(input('Nome do joagdor: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
        jogador['gols'] = gols.copy()
        jogador['total'] = sum(gols)
    list_jogadores.append(jogador.copy())
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('ERRO! Digite apenas S ou N [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=' * 30)
print(f'{"COD":<5}', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('---' * 25)
for i, v in enumerate(list_jogadores):
    print(f'{i:<5}', end='')
    for dado in v.values():
        print(f'{str(dado):<20}',end='')
    print()
print('---' * 25)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 = nenhum]: '))
    if busca == 999:
        break
    if busca >= len(list_jogadores):
        print(f'Erro! não existe jogador com o código {busca}')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {list_jogadores[busca]["nome"]}:')
        for i, g in enumerate(list_jogadores[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('---' * 25)
print('<<< ACABOU!! >>>')
