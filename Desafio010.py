print('====== DESAFIO 010 ======')

# Escreva um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input('Informe seu dinheiro: '))

cotacao = 3.27

print('Com R${:.2f}, você pode comprar U${:.2f}.'.format(real, real / cotacao))