print('====== Aula 018 ======')

# dados = list()
# dados.append('Perdro')
# dados.append(25)
# print(dados[0])
# print(dados[1])

# pessoas = list()
# pessoas.append(dados[:])
#--------------------------------
# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

# print(pessoas[0][0]) # Pedro
# print(pessoas[1][1]) # 19
# print(pessoas[2][0]) #João
# print(pessoas[1]) # ['Maria', 19]

#----------------------------------------

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

galera = [['João', 19], ['Ana', 33], ['Maria', 45]]
for g in galera:
    print(f'{g[0]} tem {g[1]} anos de idade.')

#-----------------------------------------------

pessoas = list()
dado = list()
totmaior = 0
totmenor = 0

for p in range(0, 3):
    dado.append(str(input('Nome: '))) # adicionando a lista dado o nome
    dado.append(int(input('Idade: '))) # adicionando a lista dado o idade
    pessoas.append(dado[:]) #copiando o dado para lista pessoas
    dado.clear() # limpando a lista dado
print(pessoas) #exibe todas as pessoas

for i in pessoas:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade') # exibe as pessoas maior de 21
        totmaior += 1
    else:
        print(f'{i[0]} é menor de idade') # exibe as pessoas menor de 21
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')