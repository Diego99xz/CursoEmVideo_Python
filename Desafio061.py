print('====== DESAFIO 061 ======')

#Rafaça o desafio 051, lendo o primeiro e a razão de um PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

n1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))

c = 0
while c < 10:
    print(n1)
    n1 = n1 + r
    c += 1