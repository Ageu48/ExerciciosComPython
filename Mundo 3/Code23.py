dados = []
mulheres = []
pessoasMediaAcima = []
sumIdade = 0
while True:
    pessoas = dict()
    pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().capitalize().upper()[0]
    while pessoas['sexo'] not in 'MF':
        print('ERRO! Por favor digite apenas M ou F.')
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().capitalize().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    escolha = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while escolha not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        escolha = str(input('Quer continuar? [S/N]: ')).upper()[0]
    dados.append(pessoas.copy())
    sumIdade += pessoas['idade']
    if escolha in 'Nn':
        break
mediaIdade = sumIdade / len(dados)
for p, d in enumerate(dados):
    if d['sexo'] == 'F':
        mulheres.append(d['nome'])
    if d['idade'] > mediaIdade:
        pessoasMediaAcima.append(d['nome'])
print('-=' * 30)
print(f'A) Ao todo foram cadastradas {len(dados)} pessoas.')
print(f'B) A media de idade das pessoas cadastrada é → {mediaIdade:.1F} anos.')
if len(mulheres) == 0:
    print('C) Não foi cadastrada nenhuma mulher!')
else:
    print(f'C) As mulheres cadastradas foram → {mulheres}')
if len(pessoasMediaAcima) == 0:
    print('D) Não existe pessoas com idade acima da media')
else:
    print(f'D) As pessoas com idade acima da média foram → {pessoasMediaAcima}')
print('<<<< ACABOU >>>>')
