def area():
    largura = float(input('Largura do terreno [m]: '))
    comprimento = float(input('Comprimento do terreno [m]: '))
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area}m²')


print('Controle de Terrenos')
print('-' * 20)
area()
