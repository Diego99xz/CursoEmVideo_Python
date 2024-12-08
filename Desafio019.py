print('====== DESAFIO 019 ======')

# Um professo quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

aluno_1 = str(input('Informe o nome do Primeiro aluno: '))
aluno_2 = str(input('Informe o nome do Segundo aluno: '))
aluno_3 = str(input('Informe o nome do Terceiro aluno: '))
aluno_4 = str(input('Informe o nome do Quarto aluno: '))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

# random choice escolhe um valor entre os 4
escolhido = choice(lista) 

print('O aluno escolhido foi {}'.format(escolhido))

  
