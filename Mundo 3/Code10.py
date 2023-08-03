num_list = []
while True:
    num_list.append(int(input('Digite um numero: ')))
    escolha = str(input('Quer continuar? [S/N]: '))
    if escolha in 'Nn':
        break
print('===' * 17)
print(f'Foram digitados {len(num_list)} numeros')
print(f'Os valores ordenados de forma decrescente → {sorted(num_list, reverse=True)}')
if 5 in num_list:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte lista!')
