print('---' * 12)
print('Sequência de FIBONACI!!!')
print('---' * 12)
termos = int(input('Quantos termos você quer mostrar? '))
print('~~~' * 12)
a = 0
b = 1
cont = 3
print('{} → {}'.format(a, b), end='')
while cont <= termos:
    c = a + b
    print(' → {}'.format(c),end='')
    a = b
    b = c
    cont += 1
print(' → FIM!!')
