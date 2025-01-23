print('====== DESAFIO 045 ======')

#Crieum programa que faça o computador jogar Jokenpô com você:
from random import randint
import time

print('Escolha no Jokenpô:\n[1] Pedra\n[2] Papel\n[3] Tesoura')

jogador = int(input('Escolha o número: '))
cpu = randint(1,3)

print('Jo...')
time.sleep(1)
print('Ken...')
time.sleep(1)
print('PÔ...')
time.sleep(1)



if jogador == 1 and cpu == 1:
    print('Jogador colcou Pedra')
    print('Maquinha colocou Pedra')
    print('EMPATE!')
elif jogador == 1 and cpu == 2:
    print('Jogador colcou Pedra')
    print('Maquinha colocou Papel')
    print('MAQUINHA GANHOU!')
elif jogador == 1 and cpu == 3:
    print('Jogador colcou Pedra')
    print('Maquinha colocou Tesoura')
    print('VOCÊ GANHOU!')
elif jogador == 2 and cpu == 1:
    print('Jogador colcou Papel')
    print('Maquinha colocou Pedra')
    print('VOCÊ GANHOU!')
elif jogador == 2 and cpu == 2:
    print('Jogador colcou Papel')
    print('Maquinha colocou Papel')
    print('EMPATE!')
elif jogador == 2 and cpu == 3:
    print('Jogador colcou Papel')
    print('Maquinha colocou Tesoura')
    print('MAQUINHA GANHOU!')
elif jogador == 3 and cpu == 1:
    print('Jogador colocou Tesoura')
    print('Maquinha colocou Pedra')
    print('MAQUINHA GANHOU!')
elif jogador == 3 and cpu == 2:
    print('Jogador colocou Tesoura')
    print('Maquinha colocou Papel')
    print('VOCÊ GANHOU!')
elif jogador == 3 and cpu == 3:
    print('Jogador colocou Tesoura')
    print('Maquinha colocou Tesoura')
    print('EMPATE!')
else:
    print('Opção inválida')