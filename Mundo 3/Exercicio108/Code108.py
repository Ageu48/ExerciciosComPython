from Exercicio108 import fun_numericas

valor = float(input('Digite um preço: R$ '))
print(f'A metade de {fun_numericas.moeda(valor)} é {fun_numericas.moeda(fun_numericas.metade(valor))}')
print(f'O dobro de {fun_numericas.moeda(valor)} é {fun_numericas.moeda(fun_numericas.dobro(valor))}')
print(f'Aumentando 10%, temos {fun_numericas.moeda(fun_numericas.aumentar(valor, 10))}')
