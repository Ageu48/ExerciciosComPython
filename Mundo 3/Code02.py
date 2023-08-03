tabela_brasileirao = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Athletico-PR', 'Bragantino',
                      'Fluminense', 'Flamengo', 'Ceará', 'Santos', 'Atlético-GO', 'Corinthians',
                      'Internacional', 'Juventude', 'São Paulo', 'América-MG', 'Sport', 'Cuiabá',
                      'Bahia', 'Grêmio', 'Chapecoense')
#posicao_brasileirao = ('primeira', 'segunda', 'terceira', 'quarta', 'quinta', 'sexta', 'sétima', 'oitava',
#                       'nona', 'décima', 'décima primeira', 'décima segunda', 'décima terceira', 'décima quarta',
#                       'décima quinta', 'décima sexta', 'décima sétima', 'décima oitava', 'décima nona', 'vigésima')

print(f'Os primeiros 5 times são: \033[32m{tabela_brasileirao[:5]}\033[m')
print('-=' * 48)
print(f'Os ultimos 4 colocados são: \033[32m{tabela_brasileirao[-4:]}\033[m')
print('-=' * 48)
print(f'Times em ordem alfabética: \033[32m{sorted(tabela_brasileirao)}\033[m')
print('-=' * 48)
print(f'A Chapecoense esta na \033[32m{tabela_brasileirao.index("Chapecoense") + 1}º\033[m posição')
