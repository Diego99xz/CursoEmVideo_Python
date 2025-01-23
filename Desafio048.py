print('====== DESAFIO 048 ======')

#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500

s = 0
#range
for c in range(1, 500 + 1):
    #Verifica se é impar
    if c % 2 != 0:
        #Verifica se é multiplo de 3
        if c % 3 == 0 :
            s += c
print(f'A soma dos valores é {s}')