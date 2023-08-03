print('--' * 25)


def ficha(nome='<Desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols no campeonato.'


no = str(input('Nome do jogador: '))
go = str(input('Número de gols: '))
if go.isnumeric():
    go = int(go)
else:
    go = 0
if no.strip() == '':
    print(ficha(gols=go))
else:
    print(ficha(no, go))
