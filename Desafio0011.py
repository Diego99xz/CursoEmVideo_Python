print('====== DESAFIO 011 ======')

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = int(input('Informe a largura da parede: '))
altura = int(input('Informe a altura da parede: '))

area = largura * altura
cobertura_por_litro = 2

print('Será necessário {} litros de tinta para a pintura.'.format(area/cobertura_por_litro))