print('====== DESAFIO 055 ======')

#Fala um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = []

for i in range(1, 5+1):
    peso = float(input(f'Informe o pesso da {i}º Pessoa: '))
    lista.append(peso)

print(f'O maior peso: {max(lista)}kg')
print(f'O menor peso: {min(lista)}kg')
