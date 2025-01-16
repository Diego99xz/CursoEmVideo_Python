print('====== DESAFIO 028 ======')

#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O Programador deverá escrever na tela se o usuário vencer ou não.

from random import randint

n_usuario = int(input('Informe um número de 0 a 5: '))
n_computador = randint(0,5)

if n_usuario >= 0 and n_usuario <= 5:
    if n_usuario == n_computador:
        print(f'Você acertou!!!\nO número da maquina é {n_computador}')
    else:
        print(f'Você errou!!!')
else:
    print('Numero inválido!')