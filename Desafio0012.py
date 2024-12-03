print('====== DESAFIO 012 ======')

# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = int(input('Informe o preço do Produto: '))

desconto = produto * 0.05
novo_preco = produto - desconto

print('O preço com desconto de 5% é R${:.2f}'.format(novo_preco))