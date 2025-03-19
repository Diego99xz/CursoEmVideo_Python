print('====== DESAFIO 075 ======')

#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A)Quantas vezes apareceu o valor 9.
#B)Em que posição foi digitado o primeiro valor 3.
#C)Quais foram os números pares.

n1 = int(input('Informe o Primeiro número: '))
n2 = int(input('Informe o Segundo número: '))
n3 = int(input('Informe o Terceiro número: '))
n4 = int(input('Informe o Quarto número: '))

tupla = (n1, n2, n3, n4)
nove = 0
tem_tres = 0
par = []
for i in tupla:
    if i == 9:
        nove += 1

    if i == 3:
        tem_tres = 1
        posicao = tupla.index(3) + 1
    
    if i % 2 == 0:
       par.append(i)

print(30*'-=')
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {nove} vezes') 
if tem_tres:
    print(f'O valor 3 apareceu na {posicao}º')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram {par}')
print(30*'-=')