print('====== DESAFIO 041 ======')

# A Confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua cartegoria, de acordo com a idade:

#Até 9 anos: Mirim
#Até 14 anos: infatil
#até 19 anos: junior
#Até 20 anos: Sênior
#Acima: Master

ano = int(input('Informe seu ano de nascimento: '))
idade = 2025 - ano

if idade <= 9:
    print('Categoria MIRIM!')
elif idade <= 14:
    print('Categoria INFANTIL!')
elif idade <= 19:
    print('Categoria JUNIOR!')
elif idade == 20:
    print('Categoria SÊNIOR!')
else:
    print('Categoria MASTER!')