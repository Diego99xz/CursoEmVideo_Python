print('====== Aula 022 ======')

# Módulos e Pacote

#modulo improtado para deixar o codigo mais limpo
from pacote import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')

#pacote
# pacote é uma forma de se organizar, uma pasta com modulos separados por assuntos