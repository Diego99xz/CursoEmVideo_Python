print('====== DESAFIO 035 ======')

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Informe um tamanho: '))
r2 = int(input('Informe outro tamanho: '))
r3 = int(input('Informe outro tamanho: '))

lista = sorted([r1, r2, r3])

if lista[0] + lista [1] > lista[2]:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')
