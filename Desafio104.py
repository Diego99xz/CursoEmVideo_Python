print('====== DESAFIO 104 ======')

# crie um programa que tenha a função leiaint(), que vai funcionar de forma
# semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaint('Digite um n')

def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite um número inteiro válido.')

# Programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
