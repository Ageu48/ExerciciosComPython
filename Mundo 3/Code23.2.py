pessoa = dict()
galera = list()
somaIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade das pessosas cadastrada é de {somaIdade / len(galera):.2F} anos.')
print('C) As mulheres cadastradas foram → ', end='')
for pess in galera:
    if pess['sexo'] == 'F':
        print(f'{pess["nome"]} ', end='')
print()
print('D) As pessoas com idade acima da média foram → ', end='')
for pess in galera:
    if pess['idade'] > somaIdade / len(galera):
        print(f'{pess["nome"]} com {pess["idade"]} anos. ', end='')
print()
print('<<<< ACABOU >>>>')
