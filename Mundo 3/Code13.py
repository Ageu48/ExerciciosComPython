temporario = list()
principal = list()
mai = men = 0
print(f'{"CADASTRO DE PESSOAS":=^40}')
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(int(input('Peso: ')))
    if len(principal) == 0:
        mai = men = temporario[1]
    else:
        if temporario[1] > mai:
            mai = temporario[1]
        if temporario[1] < men:
            men = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    escolha = str(input('Quer continuar? [S/N]: '))
    if escolha in 'nN':
        break
print('===' * 17)
print(f'Os dados cadastrados foram {principal}')
print(f'Foram cadastradas {len(principal)} pessoas!!')
print(f'O maior peso foi de {mai}Kg e as pessoas são → ', end='')
for pes in principal:
    if pes[1] == mai:
        print(f'[{pes[0]}]',end=' ')
print(f'\nO menor peso foi de {men}Kg e as pessoas são → ', end='')
for pes in principal:
    if pes[1] == men:
        print(f'[{pes[0]}]', end=' ')
