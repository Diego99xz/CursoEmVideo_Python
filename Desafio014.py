print('====== DESAFIO 014 ======')

# Escreva um programa que converta uma temperatura digitada é °C e converta para °F

c = float(input('Informe a temperatura: '))

f = (1.8 * c) + 32
print('A temperatura {}°C equivale a {:.2f}°F'.format(c, f))