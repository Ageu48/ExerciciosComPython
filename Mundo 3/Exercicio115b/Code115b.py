from Exercicio115b.lib.arquivo import*
from time import sleep

arquiv = 'pessoas.txt'

if not arquivoExiste(arquiv):
    criarArquivo(arquiv)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo do arquivo!
        lerArquivo(arquiv)
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        cabeçalho('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(1.5)
