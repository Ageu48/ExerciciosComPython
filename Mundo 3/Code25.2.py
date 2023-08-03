def area(largura, comprimento):
    area_do_terreno = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area_do_terreno}m²')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura [m]: '))
c = float(input('Comprimento [m]: '))
area(l, c)
