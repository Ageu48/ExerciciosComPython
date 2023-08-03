from Exercicio115c.lib.interface import *
from Exercicio115c.lib.arquivo import *
from time import sleep

arquiv = 'pessoas.txt'

if not arquivoExiste(arquiv):
    criarArquivo(arquiv)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo do arquivo.
        lerArquivo(arquiv)
    elif resposta == 2:
        # Opçao de cadastrar uma nova pessoas.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaInt('Idade: ')
        cadastrar(arquiv, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        # Digitou uma opção errada do menu.
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(1.5)
