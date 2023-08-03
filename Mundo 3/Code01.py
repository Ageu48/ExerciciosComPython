numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print('==' * 17)
print('VERIFICADOR DE NUMEROS POR EXTENSO')
print('==' * 17)
seguir = ' '
while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    if escolha < 0 or escolha > 20:
        print('Tente novamente. ', end='')
    else:
        print(f'{escolha} Por extenso fica \033[31m{numeros_por_extenso[escolha]}\033[m')
        seguir = ' '
        while seguir not in 'SN':
            seguir = str(input('Quer continuar? [S/N]')).upper()
    if seguir == 'N':
        break
print('-----' * 7)
print('Fim do programa, Volte sempre!!')
