valores_lista = []
for iten in range(0, 5):
    valores = int(input(f'Digite o valor {iten + 1}: '))
    if iten == 0 or valores > valores_lista[-1]:
        valores_lista.append(valores)
    else:
        pos = 0
        while pos < len(valores_lista):
            if valores <= valores_lista[pos]:
                valores_lista.insert(pos, valores)
                break
            pos += 1
print('==' * 28)
print(f'Os valores digitados em ordem foram → {valores_lista}', end='')
