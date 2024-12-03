print('====== DESAFIO 011 ======')

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
tinta = area /2
print('A Largura é {}m e altura é {}m a area é {}m²'.format(largura, altura, area))
print('Será necessário {} litros de tinta para a pintura.'.format(tinta))