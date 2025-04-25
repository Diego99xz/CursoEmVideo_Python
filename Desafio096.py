print('====== DESAFIO 096 ======')

# Faça um programa que tenha uma função chamada area(), que receba as dimensões
# de um terreno retangular(largura e comprimento) e mostre a área do terrno.

def area(l,c):
    r = l * c
    print(f'A área de um terreno {l}x{c} é de {r}m².')

#PROGRAMA PRINCIPAL
print(' Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
print()