from datetime import date
cadastro = dict()
print('  === cadastro de trabalhador ===  ')
cadastro['Nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = date.today().year - nascimento
cadastro['CTPS'] = int(input('Numero da CTPS \033[31m[0 = não tem!]\033[m: '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input(f'Salario de {cadastro["Nome"]} R$:'))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - nascimento
print('-=' * 30)
for k, v in cadastro.items():
    print(f'- O {k} tem o valor → {v}')
