def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opção = leiaInt('\033[32mSua Opção: \033[m')
    return opção
