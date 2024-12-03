print('====== DESAFIO 003 ======')

n = input('Digite um valor: ')
print(type(n)) #type informa o tipo primitivo da variavel
print('É um número?',n.isnumeric())
print('É alfabetico? ',n.isalpha())
print('É decimal? ',n.isdecimal())
print('Está em minúscculas? ',n.islower())
print('Está em maiúsculas? ',n.isupper())