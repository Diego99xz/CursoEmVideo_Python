print('====== DESAFIO 017 ======')

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipostenusa.
import math

cateto_oposto = float(input('informe o Cateto oposto: '))
cateto_adjacente = float(input('Informe o cateto adjacente: '))

##hispotenusa = math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)
##hispotenusa = math.sqrt(hispotenusa)

hi = math.hypot(cateto_oposto, cateto_adjacente)

print('O cateto oposto sendo {} e o Cateto adjacente sendo {} a hipotenusa é {:.2f}'.format(cateto_oposto, cateto_adjacente, hi))