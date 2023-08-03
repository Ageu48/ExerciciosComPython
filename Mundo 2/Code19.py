print('====='*6)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('====='*6)
t = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
termo = t
contador = 1
while contador <= 10:
    print('{} → '.format(termo), end='')
    termo += r
    contador += 1
print('ACABOU')
