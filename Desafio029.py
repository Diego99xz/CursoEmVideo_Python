print('====== DESAFIO 029 ======')

#Escreva um programa que leia a velocidade um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

v = int(input('Informe a velocidade KM/h: '))

if v > 80:
    km_ultrapassado = v - 80
    print('Você foi multado!\nValor da multa R$ {:.2f}'.format(km_ultrapassado*7))
else:
    print('Tenha uma boa viagem!')