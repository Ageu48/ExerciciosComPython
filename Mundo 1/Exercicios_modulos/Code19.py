valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
valor3 = float(input('Terceiro valor: '))
print('Analisando os valores {}, {} e {}'.format(valor1, valor2, valor3))
maior = valor1
menor = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3
if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
