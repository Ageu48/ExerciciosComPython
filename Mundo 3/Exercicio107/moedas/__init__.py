def aumentar(valor, taxa):
    mais = (valor * taxa/100) + valor
    return mais


def diminuir(valor, taxa):
    menos = valor - (valor * taxa/100)
    return menos


def dobro(valor):
    dobra = valor * 2
    return dobra


def metade(valor):
    met = valor / 2
    return met
