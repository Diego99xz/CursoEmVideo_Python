print('====== DESAFIO 001 ======')

#Crie um script python que leia o nome de uma pessoa e mostre uma mensagenm de boas-vindas de acordo com o valor digitado.
nome = input('Qual é seu nome? ')

#print('Olá',nome,'! Prazer em te conhecer!')
#print(f'Olá {nome}! Prazer em te conhecer!')
print('Olá {}! Prazer em te conhercer'.format(nome))