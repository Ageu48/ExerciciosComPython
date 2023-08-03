from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opções = 0
maior = primeiro
while opções != 5:
    opções = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    >>>>> Qual é a sua opção? '''))
    sleep(0.5)
    if opções == 1:
        soma = primeiro + segundo
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, soma))
    elif opções == 2:
        multiplica = primeiro * segundo
        print('A multiplicação de {} x {} é {}'.format(primeiro, segundo, multiplica))
    elif opções == 3:
        if segundo > maior:
            maior = segundo
            print('Entre {} e {} o maior valor é {}'.format(primeiro, segundo, maior))
    elif opções == 4:
        print('Informe os numeros novamente!')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif opções == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('===' * 10)
print('Fim do programa! Volte sempre!')

