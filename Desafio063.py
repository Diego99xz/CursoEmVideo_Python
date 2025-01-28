print('====== DESAFIO 063 ======')

#Escreva um programa que leia um número inteiro qualquer na tela os N primeiros elementos de uma sequencia FINONACCI

# Entrada do usuário
n = int(input("Quantos termos da sequência de Fibonacci você deseja ver? "))

n1 = 0
n2 = 1
n3 = 0
contador = 0

while contador < n:
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    contador += 1
