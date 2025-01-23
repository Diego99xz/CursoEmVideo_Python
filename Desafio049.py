print('====== DESAFIO 049 ======')

#Faça uma programa que leia um número e informe a tabuada desse número:

n = int(input('Informe o Número: '))
for i in range(0, 10 + 1):
    print(f'{n} X {i} = {i*n}')