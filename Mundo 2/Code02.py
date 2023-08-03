numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Convertido para BINARIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opção ==3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida, Tente novamente')
