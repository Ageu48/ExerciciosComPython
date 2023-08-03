print('====='*6)
print('{:^30}'.format('TERMOS DE UMA PA'))
print('====='*6)
t = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
termo = t
contador = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador < total:
        print('{} → '.format(termo), end='')
        termo += r
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!!')
