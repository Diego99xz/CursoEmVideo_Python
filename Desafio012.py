print('====== DESAFIO 012 ======')

# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Informe o preço do produto: '))
desconto = produto * 0.05
novo_preco = produto - desconto
#novo = produto - (produto * 5 / 100)
print('O Preço do produto com desconto de 5% é {}'.format(novo_preco))
