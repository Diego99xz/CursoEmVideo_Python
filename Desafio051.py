print('====== DESAFIO 051 ======')

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

for i in range(n1, r*12, r):
    print(i)