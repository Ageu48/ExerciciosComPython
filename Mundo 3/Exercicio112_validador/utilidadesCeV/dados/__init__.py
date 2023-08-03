def leiaDinheiro(vlor):
    valido = False
    while not valido:
        entrada = str(input(vlor)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO \"{vlor}\" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)
