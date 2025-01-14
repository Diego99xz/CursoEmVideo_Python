print('====== DESAFIO 016 ======')

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: digite um número: 6.127 Onúmero 6.127 tem a parte inteira 6.

from math import trunc

n1 = float(input('Informe um número flutuate: '))
inteiro = trunc(n1)
print(f'A parte inteira é {inteiro}')