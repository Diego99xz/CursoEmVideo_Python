print('====== DESAFIO 008 ======')

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

m = float(input('Informe um valor em metros: '))
c = m * 100
milimetros = m * 1000
print(f'O valor {m} Metros possui:\n{c:.2f} centímetros\n{milimetros:.2f} milimetros')