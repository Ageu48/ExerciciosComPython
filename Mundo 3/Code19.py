alunos = dict()
alunos['Nome'] = str(input('Nome do aluno: ')).capitalize().strip()
alunos['Média'] = float(input(f'Media de {alunos["Nome"]}: '))
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif 5 <= alunos["Média"] < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
print('-=' * 25)
# print(f'- Nome é igual {alunos["Nome"]}')
# print(f'- Média é igual a {alunos["Média"]:.1f}')
# print(f'- Situação de {alunos["Nome"]} é {alunos["Situação"]}')
#''''''OU'''''''
for k, v in alunos.items():
    print(f'- {k} é igual {v}')
