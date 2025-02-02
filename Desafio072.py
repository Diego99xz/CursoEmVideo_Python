print('====== DESAFIO 071 ======')

#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ser um número pelo teclado (entre 0 e 20) mostrá-lo por extenso.

numeros_ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
                'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
                'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
                'Dezoito' 'Dezenove', 'Vinte')

n = int(input('Informe um número: '))

print(f'Número por Extenso: {numeros_ext[n]}')