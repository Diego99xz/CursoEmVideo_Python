print('====== DESAFIO 018 ======')

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Informe um ângulo: '))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print('o ângulo de {}º possui o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
