pess = hom = mul20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if idade > 18:
            pess += 1
        if sexo in 'M':
            hom += 1
        if idade < 20 and sexo in 'F':
            mul20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'''{pess} pessoas tem mais de 18 anos.
{hom} homens foram cadastrados
{mul20} mulheres tem menos de 20 anos''')
