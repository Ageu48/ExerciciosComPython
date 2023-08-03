def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade > 16:
        if idade < 18 or idade >= 70:
            return f'Para idade de {idade} o voto é OPCIONAL!'
        if 18 <= idade < 70:
            return f'Para idade de {idade} o voto é OBRIGADÓRIO!'
    else:
        return f'Com a idade {idade} o voto é NEGADO!'


print(voto(int(input('Ano de nascimento: '))))
