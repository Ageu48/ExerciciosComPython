Salario = float(input('Qual o salario do funcionario? R$'))
Aumento = Salario + (Salario * 10 / 100)
Percentual = '10%'
if Salario <= 1250.00:
    Aumento = Salario + (Salario * 15 / 100)
    Percentual = '15%'
print('O seu salario antes era R${:.2F} agora com aumento de {} ficou R${:.2F}'.format(Salario, Percentual, Aumento))
