import requests

try:
    response = requests.get('http://www.pudim.com.br')
except:
    print('O site PUDIM não esta acessivel no momento')
else:
    print('O site PUDIM foi acessado com sucesso')
