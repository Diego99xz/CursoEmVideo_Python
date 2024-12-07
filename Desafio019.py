print('====== DESAFIO 019 ======')

# Um professo quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random

aluno_1 = str(input('Informe o nome do Primeiro aluno: '))
aluno_2 = str(input('Informe o nome do Segundo aluno: '))
aluno_3 = str(input('Informe o nome do Terceiro aluno: '))
aluno_4 = str(input('Informe o nome do Quarto aluno: '))

num = random.randint(1,4)

if num == 1:
    print('O aluno escolhi foi {}.'.format(aluno_1))
elif num == 2: 
    print('O aluno escolhi foi {}.'.format(aluno_2))
elif num == 3: 
    print('O aluno escolhi foi {}.'.format(aluno_3))
else:
    print('O aluno escolhi foi {}.'.format(aluno_4))    
