from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('Considerando o cateto oposto {} e cateto adjacente {} a hipotenusa do triangulo retangulo é {:.2f}'.format(co, ca, hypot(co, ca)))


