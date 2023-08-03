numero = int(input('Digite um numero inteiro: '))
div = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        div = div + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, div))
if div == 2:
    print('O numero {} é PRIMO'.format(numero))
else:
    print('{} Não é um numero primo'.format(numero))
