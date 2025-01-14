print('====== Aula 008 ======')
'''
#importa a biblioteca completa de matematica
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f}')

'''

'''
#importa os metodos especificos da biblioteca matematica
from math import sqrt, ceil

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f}')

'''

import random
n = random.randint(1, 10)
print(n)

# Biblioteca instalada via pip
import emoji

print(emoji.emojize('Feliz Natal :papai_noel: HohoHo!', language='pt'))