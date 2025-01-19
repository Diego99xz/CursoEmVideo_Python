print('====== DESAFIO 001 ======')

#Crie um script python que leia o nome de uma pessoa e mostre uma mensagenm de boas-vindas de acordo com o valor digitado.
nome = input('Qual é seu nome? ')

#print('Olá',nome,'! Prazer em te conhecer!')
#print(f'Olá {nome}! Prazer em te conhecer!')

#Lsita de cores, 0 = fecha o cod, 1 = red, 2 = green, 3 = blue
rgb = ['\033[m','\033[31m','\033[32m','\033[34m']

print('Olá {}{}{}! Prazer em te conhercer'.format(rgb[2], nome, rgb[0] ))