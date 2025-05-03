print('====== DESAFIO 106 ======')

# Faça um mini-sistema que utilize o interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

# OBS: use cores.

from time import sleep


c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - Verde
     '\033[0;30;43m',  # 2 - Amarelo
     '\033[0;30;44m',  # 2 - Azul
     '\033[0;30;45m',  # 2 - Roxo
     '\033[7;30m'      # 2 - Branco
    );



def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end = '')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo('SITEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)