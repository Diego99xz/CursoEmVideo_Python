print('====== DESAFIO 013 ======')

# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário atual: '))
aumento = salario * 0.15
novo_salario = salario + aumento
print('Seu novo salário teve o aumento de 15% e foi para {}'.format(novo_salario))