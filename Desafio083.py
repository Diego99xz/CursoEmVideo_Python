print('====== DESAFIO 083 ======')

# Crie um programa onde o usuário digite um expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = input('Digite a expressão: ')
count_abre_parenteses = 0
count_fecha_parenteses = 0

for i in range(0, len(lista)):

    if lista[i] == '(':
        count_abre_parenteses += 1
    
    if lista[i] == ')':
        count_fecha_parenteses += 1

if count_abre_parenteses == count_fecha_parenteses:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')