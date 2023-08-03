# from math import factorial
# print('Digite um numero para')
# fatorial = factorial(int(input('calcular seu fatorial: ')))
# print(fatorial)
#                                                         '''ouu'''
numero = int(input('Digite um numero para calcular o seu FATORIAL: '))
contador = numero
fatorial = 1
print('Calculando {}!'.format(numero), end=' = ')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))
