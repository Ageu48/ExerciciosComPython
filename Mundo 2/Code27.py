print('-----' * 10)
print('{:^50}'.format('LOJA DA ALEGRIA'))
print('-----' * 10)
totg = pre1000 = cont = vlor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    totg += preco
    cont += 1
    if cont == 1 or vlor > preco:
        barato = produto
        vlor = preco
    if preco > 1000:
        pre1000 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        print('===' * 9)
    if escolha == 'N':
        break
print(f'O total da compra foi R${totg:.2f}')
print(f'Temos {pre1000} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa {vlor:.2f}')
