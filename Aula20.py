print('====== Aula 020 ======')

# Funções

def mensagem(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)

mensagem('SISTEMA DE ALUNOS')
mensagem('CADASTRO DE FUNCIONÁRIOS')
mensagem('ERRO DO SISTEMA')

#---------------------------------

def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(b=3, a=2)

#--------------------------

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 5, 7, 6, 2)

#----------------------------

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

#-------------------------------

def somar(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')


somar(5, 2)
somar(2, 9, 4)