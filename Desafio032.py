print('====== DESAFIO 032 ======')

#Faça um programa que leia um ano qualqer e mostre se ele é BISSEXTO

ano = int(input('Informe um ano: '))

if ano % 4 == 0:
    ano_str = str(ano)
    if (ano_str[2:4]) == '00':
        if ano % 400 == 0:
            print('O ano {} é bissexto!'.format(ano))
        else:
            print('o ano {} não é bissexto'.format(ano))
    else:
        print('O ano {} é bissexto!'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))