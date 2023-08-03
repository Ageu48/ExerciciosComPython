def maior(*num):
    cont = maiorr = 0
    print('Analisando os valores passados...')
    for i in num:
        print(f'{i}', end=' ')
        if cont == 0:
            maiorr = i
        elif i > maiorr:
            maiorr = i
        cont += 1
    print(f'Foram informados {cont} valores ao todo...', end='')
    print(f'\nO maior valor informado é → {maiorr}')
    print('-=' * 25)


print('-=' * 25)
maior(2,4,5,7,5,4,)
maior(3,9,7)
maior(3,4)
maior(6)
maior()
