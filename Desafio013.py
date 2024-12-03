print('====== DESAFIO 013 ======')

# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário atual: '))
aumento = salario * 0.15
novo_salario = salario + aumento
print('O seu salário teve um aumento de 15% e foi para R${:.2f}'.format(novo_salario))