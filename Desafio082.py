print('====== DESAFIO 082 ======')

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o contúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
continuar = 'S'

while continuar == 'S':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    
    continuar = str(input('Quer Continuar? [S/N] ')).upper()

for i in range(0, len(lista)):

    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

print(f'Lista Completa:{lista}')
print(f'Lista Pares: {lista_par}')
print(f'Lista impares: {lista_impar}')