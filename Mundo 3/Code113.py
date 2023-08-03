def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO. Digite um numero inteiro valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[32mO usuario preferiu não digitar um valor!\033[m')
            return '→ Nenhum valor foi digitado...'
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO. Digite um numero real valido valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[32mO usuario preferiu não digitar um valor!\033[m')
            return '→ Nenhum valor foi digitado...'
        else:
            return n


num_i = leiaInt('Digite um numero Inteiro: ')
num_f = leiaFloat('Digite um numero Real: ')
print('-' * 55)
print(f'Você acabou de digitar o número {num_i}')
print(f'Você acabou de digitar o número {num_f}')
