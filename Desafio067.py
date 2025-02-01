print('====== DESAFIO 067 ======')

#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digtado pelo usuário.
#O Programa será interrompido quando o número solictado for negativo

n = 0
while True:
    n = int(input('Informe um número: '))
    if n < 0:
        break
    print(20*'-')
    for i in range(0,10+1):
        print(f'{n} X {i} = {n*i}')
    print(20*'-')

print('Programa Encerrado')