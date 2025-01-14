print('====== DESAFIO 011 ======')

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
tinta = area/2 

print(f'Será necessário {tinta:.2f}L de tinta para pintar')