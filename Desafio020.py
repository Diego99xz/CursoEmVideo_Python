print('====== DESAFIO 020 ======')

# O Professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1, n2, n3, n4] 
shuffle(lista)
print(f'A ordem de apresentação será {lista}')