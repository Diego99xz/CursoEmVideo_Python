print('====== DESAFIO 079 ======')

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

continuar = 's'
lista = []

while continuar == 's':
    valor = int(input('Digite um valor: '))
    
    if lista.count(valor):
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        lista.append(valor)


    continuar = str(input('Quer continuar? [S/N] ')).lower()

print(20*'-=-=-')
print(f'Você digitou os valores {sorted(lista)}')
