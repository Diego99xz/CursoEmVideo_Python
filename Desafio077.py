print('====== DESAFIO 077 ======')

#Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
#Depois disso, você deve mostrar, para cada palavra quais são suas vogais.

palavras = ('bola', 'galo', 'gaveta', 'chinelo','guitarra')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')