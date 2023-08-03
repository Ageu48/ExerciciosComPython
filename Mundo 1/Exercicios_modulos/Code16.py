numero = int(input('Digite um numero: '))
va = str(numero)[-1]
if va in ['0', '2', '4', '6', '8']:
    print('O numero {} é par'.format(numero))
else:
    print('O numero {} é impar'.format(numero))
