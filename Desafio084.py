print('====== DESAFIO 084 ======')

# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A)Quantas pessoas foram cadastradas.
# B)Um listagem com as pessoas mais pesadas.
# C)Um listagem com as pessoas mais leves.

pessoas = list()
pessoa = list()
continuar = 'S'
maior = 0
menor = 0
while continuar == 'S':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = str(input('quer continuar? [S/N]')).upper()

print(10*'-=-=-')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end='')