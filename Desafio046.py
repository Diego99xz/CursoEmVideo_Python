print('====== DESAFIO 046 ======')

#Faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time 

print('Contagem Regrevissa:')
for c in range(10, 0-1, -1):
    print(c)
    time.sleep(1)
print('BOOOM!!!')