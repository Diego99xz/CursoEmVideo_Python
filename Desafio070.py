print('====== DESAFIO 070 ======')

#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
'''
A)Qual é o total gasto na compra.
B)Quantos produtos custam mais de R$1000
C)Qual é o nome do produto mais barato.
'''
produtos_maior_d_mil = 0
total_gasto = 0
menor_preco = float('inf')
produto_mais_barato = ''
n = 1
while True:
    print(f'\n{n}º Produto')

    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))

    total_gasto += preco

    if preco > 1000:
        produtos_maior_d_mil += 1
    
    if preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    cotinuar = str(input('\n[S]-Sim / [N]-Não\nDeseje continuar: ')).upper().strip()

    if cotinuar == 'N':
        break

    n += 1

print(f'Total gasto {total_gasto:.2f}')
print(f'{produtos_maior_d_mil} produtos que custam mais de R$1000,00')
print(f'O produto mais barato foi {produto_mais_barato}.')