print('====== DESAFIO 101 ======')

# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

import datetime

def voto(ano):
    data_atual = datetime.date.today().year
    idade = data_atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

# PROGRAMA PRINCIPAL
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))