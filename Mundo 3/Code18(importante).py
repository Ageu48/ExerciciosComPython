print(f'{"CADASTRO DE BOLETIM DE ALUNOS":=^40}')
alunos = []
while True:
    nome_aluno = str(input('Nome do aluno: ')).strip().capitalize()
    primeira_nota = float(input('Primeira nota: '))
    segunda_nota = float(input('Segunda nota: '))
    media = (primeira_nota + segunda_nota) / 2
    alunos.append([nome_aluno, [primeira_nota, segunda_nota], media])
    escolha = str(input('Quer sair? [S/N]: ')).strip()[0]
    if escolha in 'Ss':
        break
print('-=' * 18)
print(F'{"Nº":<6}{"NOME":<12}{"MÉDIA":>8}')
for i, l in enumerate(alunos):
    print(f'{i:<6}{l[0]:<12}{l[2]:>8.1f}')
while True:
    print('--' * 18)
    opção = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(alunos) - 1:
        print(f'Notas de {alunos[opção][0]} são {alunos[opção][1]}')
print('<<< VOLTE SEMPRE >>>')

