cont = soma = 0
while True:
    num = int(input('Digite um numero [999 = PARAR]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} valores e a soma ente eles é {soma}')
