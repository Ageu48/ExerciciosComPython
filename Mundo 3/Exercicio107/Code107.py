from Exercicio107 import moedas

valor = float(input('Digite um preço: R$'))
print(f'A metade de {valor} é {moedas.metade(valor)}')
print(f'O dobro de {valor} é {moedas.dobro(valor)}')
print(f'Aumentando 10%, temos {moedas.aumentar(valor, 10)}')
