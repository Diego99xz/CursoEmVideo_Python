print('====== DESAFIO 026 ======')

# Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: '))
frase = frase.strip()
frase = frase.upper()
print(f'A frase possui {frase.count('A')} letras "A"')
print(f'A Primeira letra está "A" na posição {frase.find('A')}')
print(f'A Ultima letra está "A" na posição {frase.rfind('A')}')