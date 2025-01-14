print('====== Aula 006 ======')

# Tipos Primitivos

# int = inteiros
# float = flutuate
# bool = boleando
# str = String

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print('A soma entre', n1, 'e', n2, 'vale', s)
#print(f'A soma entre {n1} e {n2} vale {s}')
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

print('--------------------------------------')
n = input('Digite um valor: ')
print(type(n))
print(n.isnumeric())# é numerico?
print(n.isalpha())# é alfabetico?
print(n.isalnum())# é alfa númerico?
print(n.isupper())# letra maiúscula?
print(n.islower())# letra minúscula?
print(n.isprintable())# pode ser printavel?