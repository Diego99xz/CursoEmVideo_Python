print('====== DESAFIO 072 ======')

#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ser um número pelo teclado (entre 0 e 20) mostrá-lo por extenso.

n = int(input('Informe um número entre 0 e 20: '))

numeros_ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
                    'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
                    'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
                    'Dezoito' 'Dezenove', 'Vinte')

numero_valido = 0
while numero_valido == 0:
    if n > 20:
        n = int(input('Tente novamente. Informe um número entre 0 e 20: '))
    elif n < 0:
        n = int(input('Tente novamente. Informe um número entre 0 e 20: '))
    else:
        numero_valido = 1
    


print(f'Número por Extenso: {numeros_ext[n]}')