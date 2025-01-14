print('====== DESAFIO 004 ======')

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')

print('é numerico ? {}'.format(n.isnumeric()))
print('é Alfabético ? {}'.format(n.isalpha()))
print('é Alfanumérico ? {}'.format(n.isalnum()))
print('é maiúsculo ? {}'.format(n.isupper()))
print('é minúsculo ? {}'.format(n.islower()))
print('é printavel ? {}'.format(n.isprintable()))