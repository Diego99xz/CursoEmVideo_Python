print('====== DESAFIO 071 ======')

#Crie um programa que simula o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.

#OBS: Considere que o caixa possui cédulas de:
# R$ 50
# R$ 20
# R$ 10
# R$ 1

print('\nBem vindo ao Caixa eletrônico')

valor = int(input('Informe o valor para saque: '))
nota = 50
cont = 0

while valor > 0:
    if valor >= nota:
        cont = valor // nota
        valor = valor % nota
        print(f'Total de {cont} cédulas de {nota}!')
    
    if nota == 50:
        nota = 20
    elif nota == 20:
        nota = 10
    elif nota == 10:
        nota = 1

print('Obrigado por usar nosso banco!\n')