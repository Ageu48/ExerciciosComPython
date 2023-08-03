expressão = str(input('Digite a expressão: '))
pilha = []
for caractere in expressão:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Voce digitou uma expreção valida!')
else:
    print('A expreção digitada não é valida!')
