print('====== DESAFIO 052 ======')

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Verificar numeros primos ate: "))
mult=0

for c in range(2,n):
    if (n % c == 0):
        mult += 1

if(mult==0):
    print("É primo")
