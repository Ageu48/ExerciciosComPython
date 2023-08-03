from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('→ FIM!!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('→ FIM!!')


contador(1, 10, 1)
contador(10, 0, 2)
while True:
    print('-=' * 30)
    print('Agora é sua vez de personalizar a contagem!')
    ini = int(input('Digite o inicio: '))
    fi = int(input('Digite o fim: '))
    pas = int(input('Digite o passo: '))
    contador(ini, fi, pas)
    novamente = str(input('Quer tentar novamente? [S/N]: ')).strip().upper()[0]
    if novamente == 'N':
        break
print('\033[32mFim do programa. Volte sempre!!\033[32m')
