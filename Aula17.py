print('====== Aula 017 ======')

# Listas []
# Lista são mutaveis

lanche = ['Hambúrguer','Suco','Pizza','Pudim']
print(lanche)
lanche[3] = 'Sorvete' #alterando de pudim para sorvete
print(lanche)

lanche.append('Cookie') #adicionando elemento no final da lista
print(lanche)

lanche.insert(0, 'Hot-Dog') #adicionando elemento em uma posição
print(lanche)

del lanche[3] #apaga o elemento da posição
lanche.pop(3) #apaga o elemento da posição
lanche.pop() #apaga o ultimo elemento
lanche.remove('Pizza') #apaga elemento pelo nome

#Verifica se existe o elemento antes de tentar apagar
if 'Pizza' in lanche:
    lanche.remove('Pizza')

#Criando uma lista com range
valores = list(range(4, 11))

#Criando uma lista 
valores = [8,2,5,4,9,3,0]
valores.sort()#Ordenando os valores
valores.sort(reverse=True)#Ordenando ao contrario

len(valores) # Conta os elementos da lista

#printar valores sem formatação de lista
for v in valores:
    print(f'{v}...', end='')


#printar valores e chave sem formatação de lista
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


#lista de valores do teclado
valores_teclado = list()
for cont in range(0, 5):
    valores_teclado.append(int(input('Digite um valor: ')))

#conectar uma lista em outra
a = [2, 3, 4, 7]
b = a #todas as alterações feitas na lista a ou b atualizará as 2 listas

#criar uma cópia da lista
b = a[:]