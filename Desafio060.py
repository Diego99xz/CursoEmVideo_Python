print('====== DESAFIO 060 ======')

#faça um programa que leia número qualquer e mostre o seu fatorial.
#EX:
# 5 = 5x4x3x2x1 = 120

n = int(input('Informe um número: '))
fatorial = n - 1
r = 0
acumulado = n*fatorial

while fatorial != 1:
    fatorial -= 1
    acumulado = acumulado * fatorial

    print(acumulado)
    print(fatorial)
    print("-----------")

print(f'O Fatorial de {n} é {acumulado}')