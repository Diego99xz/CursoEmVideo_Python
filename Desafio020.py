print('====== DESAFIO 020 ======')

# O Professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

# Lendo os nomes dos alunos
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

# Criando uma lista com os nomes
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralhando a lista
shuffle(alunos)

# Mostrando a ordem sorteada
print('A ordem de apresentação será:')
print(alunos)