valores_lista = [int(input('Digite um valor: ')),
                 int(input('Digite um valor: ')),
                 int(input('Digite um valor: ')),
                 int(input('Digite um valor: ')),
                 int(input('Digite um valor: '))]
print(f'Os valores digitados foram → {valores_lista}')
print(f'O maior valor digitado foi {max(valores_lista)} e sua posição na lista é'
      f' {valores_lista.index(max(valores_lista)) + 1}')
print(f'O menor valor digitado é {min(valores_lista)} e sua posição na lista é'
      f' {valores_lista.index(min(valores_lista)) + 1}')
