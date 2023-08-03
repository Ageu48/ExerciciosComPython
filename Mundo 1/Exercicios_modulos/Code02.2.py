co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Considerando cateto oposto {} e cateto adjacente {} a hipotenusa do triangulo retangulo será {:.2f}'.format(co, ca, hi))


