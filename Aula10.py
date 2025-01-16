print('====== Aula 010 ======')

#Condições

'''
nome = str(input('Qual é seu nome? '))
if nome == 'Diego':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))
'''

'''
#cCondição Composta
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro Velho')
print('--FIM--')
'''

'''
#Condição simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo'if tempo<=3 else'Carro velho')
print('--FIM--')
'''

#Condição Composta
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

'''
#Condição simples
print('PARABÉNS!' if m>=6 else'ESTUDE MAIS!')
'''
