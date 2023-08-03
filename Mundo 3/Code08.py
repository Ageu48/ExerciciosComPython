valores_lista = []
escolha = ' '
while True:
    valores = int(input('Digite um valor: '))
    if valores not in valores_lista:
        valores_lista.append(valores)
        print('Valor adicionado com sucesso...')
    else:
        print('O valor foi duplicado! Não vou adicionar...')
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]: ')).upper()
    if escolha in 'N':
        break
    else:
        escolha = ' '
print('==' * 17)
print(f'Você digitou os valores{sorted(valores_lista)}', end='')
