print('====== DESAFIO 040 ======')

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#Média abaixo de 5: Reprovado
#Média entre 5 e 6.9: Recuperação
#Média 7 ou superior: Aprovado

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

m = (n1+n2)/2

if m >= 7:
    print('Aprovado!')
elif m >= 5 and m <= 6.9:
    print('Recuperação!')
else:
    print('Reprovado!')