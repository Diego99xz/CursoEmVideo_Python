print('====== DESAFIO 097 ======')

# Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como 
#  parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex
# escreva('Olá, mundo!')

# saida
#---------------
# Olá, mundo!
#---------------

def escreva(msg):
    tamanho = len(msg) + 4
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)

#PROGRAMA PRINCIPAL
mensagem = str(input('Escreva uma mensagem: '))
escreva(mensagem)