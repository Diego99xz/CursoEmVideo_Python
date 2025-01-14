print('====== DESAFIO 021 ======')

# Faça um programa en python que abra e reproduza o áudio de um arquivo mp3

from pygame import mixer

mixer.init()
mixer.music.load('Desafio021b.mp3')
mixer.music.play()
stop = input('Digite algo para parar...')