print('====== DESAFIO 018 ======')

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

n = float(input('Informe um ângulo: '))
rad = radians(n)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')
