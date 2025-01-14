print('====== DESAFIO 019 ======')

# Um professo quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
sorteado = choice([n1, n2, n3, n4])
print(f'O Aluno que vai apagar a lousa é {sorteado}')