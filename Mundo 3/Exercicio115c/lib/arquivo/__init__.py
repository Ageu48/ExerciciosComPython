from Exercicio115c.lib.interface import *


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
        for linha in abrir:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        abrir.close()


def cadastrar(arquivo, nome='Não informado', idade='0'):
    try:
        abrir = open(arquivo, 'at')
    except:
        print('Houve um ERRO ao tentar abrir o arquivo!')
    else:
        try:
            abrir.write(f'{nome};{idade}\n')
        except:
            print('Ocorreu um ERRO ao tentar incluir os dados no arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            abrir.close()
