print('====== DESAFIO 076 ======')

#Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

material = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print(20*'-=')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(20*'-=')
for pos in range(0, len(material)):
    if pos % 2 == 0:
        print(f'{material[pos]:.<30}', end='')
    else:
        print(f'R${material[pos]:>7.2f}')

print(20*'-=')
