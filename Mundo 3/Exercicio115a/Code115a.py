from Exercicio115a.lib.interface import*
from time import sleep
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        cabeçalho('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(1.5)
