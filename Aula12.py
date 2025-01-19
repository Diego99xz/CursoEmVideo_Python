print('====== Aula 012 ======')

#Concições Aninhadas

nome = str(input('Qual é seu nome? '))

#Condição simples
if nome == 'Diego':
    print('Que nome bonito!')

#Estrutura condicional composta
if nome == 'Gustavo':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')

#Estrutura condicional Aninhada
if nome == 'Jessica':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Gorete Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')


print('Tenha um bom dia {}'.format(nome))