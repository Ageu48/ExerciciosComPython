sexo = str(input('Qual é o seu sexo: [M/F]? ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe o seu sexo: ')).upper()
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('\033[32mSexo {} Registrado'.format(sexo.upper()))
