num_list = []
num_listpar = []
num_listimpar = []
while True:
    num_list.append(int(input('Digite um valor: ')))
    escolha = str(input('Quer continuar? [S/N]: '))
    if escolha in 'Nn':
        break
for v in num_list:
    if v % 2 == 0:
        num_listpar.append(v)
    else:
        num_listimpar.append(v)
print(f'Os valores incluido na lista foram → {num_list}')
print(f'A lista somente com valores pares → {num_listpar}')
print(f'A lista com os valores impares → {num_listimpar}')
