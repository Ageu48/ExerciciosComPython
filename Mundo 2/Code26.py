pessoas18 = homens = mulheres20 = cont = 0
print('{:=^40}'.format('CADASTRO DE PESSOAS'))
while True:
    cont += 1
    print(f'---------Pessoa {cont}---------')
    nome = str(input('Digite o nome: ')).strip()[0]
    idade = int(input('Digite a idade: '))
    if idade > 18:
        pessoas18 += 1
    sexo = str(input('Digite o sexo [M/F]: ')).strip()[0]
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres20 += 1
    print('==' * 11)
    para = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if para == 'N':
        break
print('-------' * 10)
print('Fim do programa!!')
print(f'''{pessoas18} Pessoas tem mais de 18 anos
{homens} Homens foram cadastrados
{mulheres20} Mulheres tem menos de 20 anos''')
