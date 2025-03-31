print('====== DESAFIO 078 ======')

# Faça um programa que leia 5 valores numérios e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições

lista = []

for i in range(0, 5):
    n = int(input(f'Digite um valor para a posição {i}: '))
    lista.append(n)

print(20*'-=-=-')
print(f'Você Digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições {lista.index(max(lista))}...')
print(f'O menor valor digitado foi {min(lista)} nas posições {lista.index(min(lista))}...')