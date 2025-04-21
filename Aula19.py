print('====== Aula 019 ======')

# Tuplas ()
# Listas []
# Dicionários {}

dados = {
    'nome':'Pedro',
    'idade': 25
}

dados['sexo'] = 'M' # adicionando novo elemento
del dados['sexo'] # deletando elemento
print(dados['nome'])
print(dados['idade'])
#-----------------------------------
filme = {
    'titulo':'Star Wars',
    'ano': 1977,
    'diretor':'George Lucas'
}

print(filme.values()) #Valores
print(filme.keys()) #Chaves
print(filme.items()) #itens

for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values()) #valores
print(pessoas.keys()) #chaves
print(pessoas.items()) #itens

for v in pessoas.values():
    print(v)

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'Leandro' # alterando o nome
pessoas['peso'] = 98.5 # adicionar novos items

#----------------------------------------------
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

#--------------------------------------------------
estados = dict() # dicionário
brasil = list() #lista 
for c in range(0, 3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estados.copy())
print(brasil)

for e in brasil: #vai percorrer a lista
    for k, v in e.items(): #vai percorrer o dicionário
        print(f'O campo {k} tem valor {v}.')
