print('====== DESAFIO 014 ======')

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

distancia = float(input('Informe quantos KM foi percorridos: '))
dias = int(input('Informe quantos dias de aluguel: '))

total = (distancia * 0.15) + (dias * 60)
print('O valor total a pagar é de R${:.2f}'.format(total))