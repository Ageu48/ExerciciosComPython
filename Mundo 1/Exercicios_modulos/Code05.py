from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação do trabalho é {}'.format(lista))

# from random import sample
# a1 = str(input('Primeiro aluno: '))
# a2 = str(input('Segundo aluno: '))
# a3 = str(input('Terceiro aluno: '))
# a4 = str(input('Quarto aluno: '))
# lista = [a1, a2, a3, a4]
# ordem = sample(lista, k=4)
# print('A ordem de apresentação do trabalho é {}'.format(ordem))





