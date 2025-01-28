print('====== DESAFIO 065 ======')

#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usu´´ario se ele quer ou não continuar a digitar valores.

continuar = 'S'
lista = []
while continuar != 'N':
    n = int(input('Informe um valor: '))
    lista.append(n)
    continuar = str(input('você quer continuar a digitar valores:\n[S]Sim\n[N]Não\nDigite a letra da opção: '))
    continuar = continuar.upper()
    
soma = sum(lista)
maior = max(lista)
menor = min(lista)
print('A Média é {}'.format(soma/len(lista)))
print('O Maior número é {}'.format(maior))
print('O Menor número é {}'.format(menor))
print('Programa Encerrado!')