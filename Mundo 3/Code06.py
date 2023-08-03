tupla = ('mamona', 'banana', 'carro', 'computador', 'praia', 'guitarra', 'chocolate', 'amarelo', 'cinema', 'flor')
for palavra in tupla:
    print(f'\nNa palavra---{palavra.capitalize():-<15}temos → ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
            