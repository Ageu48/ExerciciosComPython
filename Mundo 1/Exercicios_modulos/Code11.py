frase = str(input('Digite uma frase: ')).strip()
print('Na frase: {}\nO caractere A aparece {} vezes na frase {} '.format(frase, frase.upper().count('A'), frase))
print('O caractere [A] aparece primeiro na posição: {} & a ultima vez que aparece é na posição: {}'.format(frase.upper().find('A')+1, frase.upper().rfind('A')))
