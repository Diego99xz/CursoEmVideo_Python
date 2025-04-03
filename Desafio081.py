print('====== DESAFIO 081 ======')

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A)Quantos números foram digitados
# B)A lista de valores, ordenada de forma decrescente.
# C)Se o valor 5 foi digitados e está ou não na lista.

lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    continuar = input('Quer continuar? [S/N] ').strip().lower()
    if continuar != 's':
        break

lista.sort(reverse=True)  # Ordena a própria lista

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')  # Imprime a lista corretamente
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não está na lista!')