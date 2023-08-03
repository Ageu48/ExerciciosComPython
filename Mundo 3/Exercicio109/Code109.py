import fun_numericas

valor = float(input('Digite um preço: R$ '))
print(f'A metade de {fun_numericas.moeda(valor)} é {fun_numericas.metade(valor, True)}')
print(f'O dobro de {fun_numericas.moeda(valor)} é {fun_numericas.dobro(valor,True)}')
print(f'Aumentando 10%, temos {fun_numericas.aumentar(valor, 10, True)}')
print(f'Diminuindo 15%, temos {fun_numericas.diminuir(valor, 15, True)}')
