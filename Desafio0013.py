print('====== DESAFIO 013 ======')

# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = int(input('Informe o salário atual: '))
aumento = salario * 0.15
novo_salario = salario + aumento
print('O seu salário teve um aumento de 15% e foi para R${}'.format(novo_salario))