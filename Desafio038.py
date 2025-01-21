print('====== DESAFIO 038 ======')

#Escreva um progra que leia dois números inteiros e compare-os mostrando na tela uma mensage:
# O Primeiro valor é Maior
# O Segundo valor é Maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))

if n1 > n2:
    print(f'O Primeiro valor é maior!')
elif n1 < n2:
    print('O segundo valor é maior!')
else: 
    print('Não existe valor maior, os dois são iguais!')