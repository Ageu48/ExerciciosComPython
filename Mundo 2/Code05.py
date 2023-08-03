from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
data_atual = date.today().year
idade = data_atual - ano
print('Quem nasceu em {} tem {} Anos.'.format(ano, idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
