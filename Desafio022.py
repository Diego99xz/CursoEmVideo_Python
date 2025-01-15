print('====== DESAFIO 022 ======')

#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome.

nome_completo = str(input('Nome Completo: '))
nomes = nome_completo.split()
print('Nome em Maiúsculo: {}'.format(nome_completo.upper()))
print('Nome em Minúsculo: {}'.format(nome_completo.lower()))
print('Quantidade de letras nome completo: {}'.format(len(nome_completo.replace(' ',''))))
print('Quantidade de letras primeiro nome: {}'.format(len(nomes[0])))