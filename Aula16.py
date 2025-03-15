print('====== Aula 016 ======')

# tupla = ()
# lista = []
# dicionario = {}

#As Tuplas são imutáveis, ou sejá não pode trocar os valores dos itens

lanche = ('Hambúrguer','Suco','Pizza','Pudim')

print(lanche[2]) #item do indice 2
print(lanche[0:2])#itens do indice 0 até o 2 monstrando somente item 0 e 1
print(lanche[1:])#itens do indice 1 até o fim
print(lanche[-1])#Último item do indice
print(lanche[-2])#Penúltimo item do indice
print(lanche[-2:])#Os dois útimos itens
print(len(lanche))#conta a quantidade de itens
print(sorted(lanche))#Organizou na ordem, neste alfabetica
print('\n------------------')

for i in lanche:
    print(f'Eu vou comer {i}')

print('\n------------------')

for cont in range(0, len(lanche)):
    print(lanche[cont])

print('\n------------------')

for posicao, comida, in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

print('\n------------------')

print(sorted(lanche))# Imprime em ordem. no caso alfabetica que tambem está transformando em lista
print('\n------------------')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 
print(c)#União da tupla A com a tupla B
print(len(c))#Tamanho da taupla c
print(c.count(5))#Quantas vezes está aparecendo o número 5 dentro da tupla C
print(c.index(8))#Informa em que posição está o número 8
print(c.index(5,1))#Ele informa a posição que está o número 5 começando apartir da posiçãom 1, ingnorando a posição zero.

pessoa = ('Diego', 32, 'M', 99.88)# Nas Tuplas de tipos Diferentes
print(pessoa)
del(pessoa)#Comando usado para apagar uma variável, 
#A tupla é imutável, mas ela pode ser apagada por completa, porem não pode ser apagada somente item.