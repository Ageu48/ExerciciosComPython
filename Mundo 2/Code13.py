print('====='*6)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('====='*6)
t = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
decimo = t + (10 - 1) * r
for pa in range(t, decimo + r, r):
    print(pa, end=' → ')
print('ACABOU')
