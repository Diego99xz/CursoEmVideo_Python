print('====== DESAFIO 039 ======')

#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.

ano = int(input('Informe seu ano de nascimento: '))
idade = 2025 - ano

if idade == 18:
    print('Hora de se alistar!')
elif idade < 18:
    tempo = 18 - idade
    print('Ainda vai se alistar!')
    print(f'Falta {tempo} anos')
elif idade > 18:
    tempo = idade -18
    print('Passou do tempo de se alistar!')
    print(f'Passou {tempo} anos do prazo')