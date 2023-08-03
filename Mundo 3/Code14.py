vlor_list = [[], []]
vlor = 0
for lista in range(1, 8):
    vlor = (int(input(f'Digite o valor {lista}º: ')))
    if vlor % 2 == 0:
        vlor_list[0].append(vlor)
    else:
        vlor_list[1].append(vlor)
print('===' * 22)
print(f'O valores cadastrados na lista foram → {vlor_list}')
print(f'Os valores pares são → {sorted(vlor_list[0])}')
print(f'Os valores impares são → {sorted(vlor_list[1])}')
