print('====== DESAFIO 008 ======')

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

metros = int(input('Informe a quantidade de metros: '))

centimetros = metros * 100
milimetros = metros * 1000
print('{}metro(s) possui {} centimetros e {} milimetros.'.format(metros, centimetros, milimetros))