print('====== DESAFIO 085 ======')

# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = list()
lista_impar = list()
lista_par = list()

cont = 1

while cont < 8:

    lista.append(int(input(f'Digite o {cont}º valor: ')))

    if lista[cont -1] % 2 == 0:
        lista_par.append(lista[cont -1])
    else:
        lista_impar.append(lista[cont -1])
    
    cont += 1
print(15*'-=-=-')
print(f'Os valores pares digitados foram: {lista_par}')
print(f'Os valores Ímpares digitados foram: {lista_impar}')