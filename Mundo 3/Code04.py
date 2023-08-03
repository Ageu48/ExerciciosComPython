cont9 = 0
valores = (int(input('Digite um numero: ')),
           int(input('Digite otro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 tem {valores.count(9)} ocorrencias')
if 3 in valores:
    print(f'O valor 3 foi digitado na posição {valores.index(3) + 1}ª')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os numeros pares foram: ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
