print('{:=^40}'.format('TABUANDA DA LOCURA if == negativo o programa para'))
while True:
    num = int(input('Quer ver tabuada de qual valor? '))
    print('----' * 10)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('----' * 10)
print('Fim do programa!!!')
