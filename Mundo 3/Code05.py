frutas = ('banana', 12.00, 'maçã', 7.50, 'laranja', 5.99, 'abacaxi',
          10.25, 'uva', 8.75, 'melancia', 15.05, 'limão', 3.50,
          'morango', 12.99, 'pera', 6.80, 'kiwi', 9.15)
print('-' * 38)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 38)
for posição in range(0, len(frutas)):
    if posição % 2 == 0:
        print(f'{frutas[posição]:.<30}'.capitalize(), end='R$ ')
    else:
        print(f'{frutas[posição]:.2F}')
print('-' * 38)
