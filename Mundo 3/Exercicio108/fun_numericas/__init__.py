def aumentar(valor=0, taxa=0):
    mais = (valor * taxa / 100) + valor
    return mais


def diminuir(valor=0, taxa=0):
    menos = valor - (valor * taxa / 100)
    return menos


def dobro(valor=0):
    dobra = valor * 2
    return dobra


def metade(valor=0):
    met = valor / 2
    return met


def moeda(valor=0, na='R$'):
    moe = f'{na}{valor:.2F}'.replace('.', ',')
    return moe
