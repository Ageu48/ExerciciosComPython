from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
data_atual = date.today().year
sexo = input('Digite o seu sexo:').strip().upper()
print('\033[32mQuem nasce em {} tem ou faz {} qnos em {}'.format(ano, data_atual - ano, data_atual))
if data_atual - ano > 18 and sexo == 'MASCULINO':
    print('\033[31mVocê ja devia ter se alistado a {} anos!!\n'
          'O seu alistamento foi em {}'.format(data_atual - ano - 18, ano + 18))
elif data_atual - ano < 18 and sexo == 'MASCULINO':
    print('\033[31mAinda faltam {} anos para que você tenha que se alistar\n'
          'O seu alistamento sera em {}'.format(18 - (data_atual - ano), ano + 18))
elif data_atual - ano == 0 and sexo == 'MASCULINO':
    print('\033[31mVocê deve se alistar IMEDIATAMENTE!')
else:
    print('\033[31mVocê não precisa se alistar!!!')

