casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salario do comprador: R$'))
anos = int(input('Quanto anos de financiamento?'))
prestação = casa / (anos * 12)
print('Para pagar uma casa de R${:.2F} em {} anos a prestação será R${:.2F}'.format(casa, anos, prestação))
if prestação > salario * (30 / 100):
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO')
