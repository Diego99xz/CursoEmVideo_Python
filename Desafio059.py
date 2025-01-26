print('====== DESAFIO 059 ======')

'''
#Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
seu programa deverá realizar a operação solicitada em cada caso
'''

sair = 0

n1 = int(input('Informe umnúmero: '))
n2 = int(input('Informe outro número: '))
while sair != 5:
    
    opcao = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\nEscolha aopção desejada: '))

    if opcao == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opcao == 2:
        print(f'{n1} X {n2} = {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        else:
            print('O Dois números são iguais!')
    elif opcao == 4:
        n1 = int(input('Informe umnúmero: '))
        n2 = int(input('Informe outro número: '))
    elif opcao == 5:
        sair = 5
    else:
        print('Opção inválida')
print('Programa Encerrado!')