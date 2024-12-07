print('====== DESAFIO 016 ======')

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# EX: digite um número: 6.127 Onúmero 6.127 tem a parte inteira 6.

import math
num = float(input('Informe um número real: '))
print('O número {} tem a parte inteira {}'.format(num, math.floor(num)))
