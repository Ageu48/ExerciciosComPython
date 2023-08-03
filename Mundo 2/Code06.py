print('ANALISADOR DE TRIANGULOS!!')
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os seguimentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
     print('Os segmentos acima NÃO podem formar um triângulo')

