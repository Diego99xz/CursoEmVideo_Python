print('====== DESAFIO 068 ======')

#Faça um programa que jogue par ou impar com o computador.
#O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.

from random import randint

v = 0
while True:
    jogador_escolha = str(input('[I]-Impar\n[P]-Par\nEscolha entre impar ou Par: '))
    jogador_numero = int(input('Escolha seu número: '))
    jogador_escolha = jogador_escolha.upper()

    cpu_numero = randint(1,2)
    resultado = jogador_numero + cpu_numero
    print(15*'=-=')
    if jogador_escolha == 'I':
        print('Jogador Escolheu Impar')
        if resultado % 2 != 0:
            print(f'Jogador escolheu número {jogador_numero}')
            print(f'CPU escolheu {cpu_numero}')
            print(f'Resultado foi IMPAR: {resultado}')
            print(f'Parabens!')
            v += 1
        else:
            print(f'Jogador escolheu número {jogador_numero}')
            print(f'CPU escolheu {cpu_numero}')
            print(f'Resultado foi PAR: {resultado}')
            print('GAMER OVER!')
            break
    elif jogador_escolha == 'P':
        print('Jogador Escolheu Par')
        if resultado % 2 == 0:
            print(f'Jogador escolheu número {jogador_numero}')
            print(f'CPU escolheu {cpu_numero}')
            print(f'Resultado foi PAR: {resultado}')
            print(f'Parabens!')
            v += 1

        else:
            print(f'Jogador escolheu número {jogador_numero}')
            print(f'CPU escolheu {cpu_numero}')
            print(f'Resultado foi IMPAR: {resultado}')
            print('GAMER OVER!')
            break
    else:
        print('Escolha incorrenta!')
    print(15*'=-=')
print(f'Você Ganhou {v} vezes da maquina')
print('Programa Encerrado!')