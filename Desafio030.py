print('====== DESAFIO 030 ======')

#Crie um programa que leia um número inteiroe mostre na tela se ele é PAR ou IMPAR

n = int(input('Informe um número: '))
if n % 2 == 0:
    print(f'{n} é um número PAR')
else:
    print(f'{n} é um número IMPAR')