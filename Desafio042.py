print('====== DESAFIO 042 ======')

#Refaça o desafio 35 dos triângulos, acrescentando o recuso de mostar que tipo de triângulo será formado:
#Equilátero: Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes


r1 = int(input('Informe um tamanho: '))
r2 = int(input('Informe outro tamanho: '))
r3 = int(input('Informe outro tamanho: '))

lista = sorted([r1, r2, r3])

if lista[0] + lista [1] > lista[2]:
    print('As retas formam um triângulo!')

    if lista[0] == lista[1] == lista[2]:
        print('Triângulo Equilátero!')
    elif lista[0] != lista[1] != lista[2]:
        print('Triângulo Escaleno!')
    else:
        print('Triângulo Isósceles!')
else:
    print('As retas não formam um triângulo!')