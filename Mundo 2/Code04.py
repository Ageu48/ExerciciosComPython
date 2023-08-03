n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média foi {:.2F} \033[31mREPROVADO'.format(media))
elif media >= 7:
    print('Sua media foi {:.2F} \033[32mAPROVADO'.format(media))
else:
    print('Sua media foi {:.2F} \033[33mVocê esta de RECUPERAÇÃO'.format(media))
