print('====== DESAFIO 021 ======')

# Faça um programa en python que abra e reproduza o áudio de um arquivo mp3

# importar a biblioteca pygame
from pygame import mixer

# inicia o mixer
mixer.init()
# carrega o arquivo mp3
mixer.music.load('Desafio021b.mp3')
# Executa o arquivo mp3
mixer.music.play()

x = input('Digite algo para parar a música...')