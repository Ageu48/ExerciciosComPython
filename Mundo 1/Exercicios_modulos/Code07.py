nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome todo maiusculo é {} '.format(nome.upper()))
print('Seu nome todo minusculo é {} '.format(nome.lower()))
print('Seu nome completo é {} e possui {} Letras '.format(nome.title(),len(nome.replace(" ",""))))
print('Seu primeiro nome é {} e possui {} Letras'.format(nome.split()[0],len(nome.split()[0])))




