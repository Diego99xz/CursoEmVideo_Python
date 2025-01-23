print('====== DESAFIO 050 ======')

#Desenvolva um progra que leia seis números inteiros e mostre a soma apenas daqueles que foram pares. Se o valor digitado for ímpar, descondire-o:

s=0
for i in range(0, 6):
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos números pares é {s}')
