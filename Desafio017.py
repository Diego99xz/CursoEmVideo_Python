print('====== DESAFIO 017 ======')

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipostenusa.

from math import hypot

co = float(input('informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
h = hypot(co, ca)
print(f'O valor da Hipotenusa é {h:.2f}')