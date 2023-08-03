from Exercicio115b.lib.interface import *


def arquivoExiste(nome):
    try:
        abrir = open(nome, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        abrir = open(nome, 'wt+')
        abrir.close()
    except:
        print('Ocorreu um erro ao tentar criar o arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        abrir = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(abrir.readlines())
