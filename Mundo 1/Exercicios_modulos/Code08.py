num = int(input('Informe um valor: '))
print('Analisando o número {}'.format(num))
# print('Unidades: {}'.format(len(str(num))))
print('Unidades: {}'.format(num // 1 % 10))
print('Dezenas: {}'.format(num // 10 % 10))
print('Centenas: {}'.format(num // 100 % 10))
print('Milhar {}'.format(num // 1000 % 10))

