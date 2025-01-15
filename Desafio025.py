print('====== DESAFIO 025 ======')

#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Informe seu nome: '))
nome = nome.upper()
print('A pessoa tem "SILVA" no nome ?')
print('SILVA' in nome)