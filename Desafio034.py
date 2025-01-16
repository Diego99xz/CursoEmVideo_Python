print('====== DESAFIO 034 ======')

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00 calcule um aumento de 10%
#Para os interiores ou iguais, o aumento é de 15%

salario = float(input('Informe o salário: '))
if salario > 1250:
    print('Você recebeu um aumento de 10%')
    print('Seu salário atual é R$ {}'.format(salario+((salario*10)/100)))
else:
    print('Você recebeu um aumento de 15%')
    print('Seu salário atual é R$ {}'.format(salario+((salario*15)/100)))
