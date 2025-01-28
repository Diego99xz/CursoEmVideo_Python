print('====== DESAFIO 064 ======')

#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#no final, mostre quantos números foram digitados e qual foi a soma entre eles.

soma = 0
lista = []
n = 0
while n != 999:
    n = int(input('Digite outro número: '))
    if n == 999:
        break

    lista.append(n)
    soma += n
print(f'Os números digitados foram {lista}')
print(f'A soma dos número é {soma}')