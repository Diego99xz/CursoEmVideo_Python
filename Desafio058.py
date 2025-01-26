print('====== DESAFIO 058 ======')

#Melhorem o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora  o jogador vai tentar adivinhar até acertar, mostrando no final quantos paplpites foram necessários para vencer.


from random import randint


tentativas = 0
n_computador = randint(0,10)
n_usuario = 100
while n_computador != n_usuario:
    n_usuario = int(input('Informe um número de 0 a 5: '))

    if n_usuario >= 0 and n_usuario <= 10:
        if n_usuario == n_computador:
            print(f'Você acertou!!!\nO número da maquina é {n_computador}')
            tentativas += 1 

        else:
            print(f'Você errou!!!')
            tentativas += 1 
    else:
        print('Numero inválido!')

print(f'Número de tentativas {tentativas}')