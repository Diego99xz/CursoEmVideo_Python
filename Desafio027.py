print('====== DESAFIO 027 ======')

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#EX: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome_completo = str(input('Informe o nome completo: '))
nomes = nome_completo.split()
print(f'Primeiro: {nomes[0]}')
print(f'Último: {nomes[-1]}')