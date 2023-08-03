print('=-' * 15)
print('Analisador de Triângulos')
print('=-' * 15)
A = float(input('Primeiro seguimento: '))
B = float(input('Segundo seguimento: '))
C = float(input('Terceiro segmento: '))
if A + B > C and A + C > B and B + C > A:
    print('Os seguimentos {}, {} & {} PODEM FORMAR um triângulo' .format(A, B, C))
else:
    print('Os segmentos {}, {} & {} NÃO podem formar um triângulo'.format(A, B, C))
