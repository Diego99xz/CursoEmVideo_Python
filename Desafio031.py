print('====== DESAFIO 031 ======')

#Desenvolva um programa que pergunta a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.

d = int(input('Informe a distância da viagem em KM: '))

if d <= 200:
    print('O preço da viagem é R$ {:.2f}'.format(d * 0.5))
else:
    print('O preço da viagem é R$ {:.2f}'.format(d * 0.45))