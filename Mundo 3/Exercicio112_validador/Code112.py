from Exercicio112_validador.utilidadesCeV import moeda
from Exercicio112_validador.utilidadesCeV import dados

valor = dados.leiaDinheiro('Digite o valor R$')
moeda.resumo(valor, 3, 20, True)
