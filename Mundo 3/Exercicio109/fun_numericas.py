def aumentar(valor=0, taxa=0, formata=False):
    """
    Função que aumenta um valor pela taxa percentual fornecida.

    :param valor: Valor inicial a ser aumentado.
    :param taxa: Taxa percentual de aumento.
    :param formata: Indica se o valor deve ser formatado como moeda.
    :return: Valor aumentado pela taxa percentual, ou valor formatado como moeda, se formata for True.
    """
    mais = (valor * taxa / 100) + valor
    return mais if formata is False else moeda(mais)


def diminuir(valor=0, taxa=0, formata=False):
    """
    Função que diminui um valor pela taxa percentual fornecida.

    :param valor: Valor inicial a ser diminuído.
    :param taxa: Taxa percentual de diminuição.
    :param formata: Indica se o valor deve ser formatado como moeda.
    :return: Valor diminuído pela taxa percentual, ou valor formatado como moeda, se formata for True.
    """
    menos = valor - (valor * taxa / 100)
    return menos if formata is False else moeda(menos)


def dobro(valor=0, formata=False):
    """
    Função que retorna o dobro de um valor.

    :param valor: Valor a ser dobrado.
    :param formata: Indica se o valor deve ser formatado como moeda.
    :return: Dobro do valor, ou valor formatado como moeda, se formata for True.
    """
    dobra = valor * 2
    if formata:
        return moeda(dobra)
    return dobra


def metade(valor=0, formata=False):
    """
    Função que retorna a metade de um valor.

    :param valor: Valor a ser dividido pela metade.
    :param formata: Indica se o valor deve ser formatado como moeda.
    :return: Metade do valor, ou valor formatado como moeda, se formata for True.
    """
    met = valor / 2
    if formata:
        return moeda(met)
    return met


def moeda(valor=0, na='R$'):
    """
    Função que formata um valor como uma string de moeda.

    :param valor: Valor a ser formatado.
    :param na: Símbolo da moeda. O padrão é 'R$'.
    :return: Valor formatado como uma string de moeda.
    """
    moe = f'{na}{valor:.2F}'.replace('.', ',')
    return moe
