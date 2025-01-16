print('====== DESAFIO 033 ======')

#Faça um programa que leia três números e mostre qual é o maior e qual é menor

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
n3 = int(input('Informe outro número: '))
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')