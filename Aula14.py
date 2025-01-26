print('====== Aula 014 ======')

#Estrutura de repetição While

i = 1
while i < 10:
    print(i)
    i += 1
print('Fim')

# While é perfeito para quando você não sabe definir o final do loop

#Enquanto o valor digitado não for 0 continua
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

#Enquanto o valor digitado for S, o programa vai continuar
r= 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')



#Equanto não digitar zero o loop continua
par = 0
impar = 0
x = 1
while x != 0:
    x = int(input('Digite um valor: '))
    if x != 0:#invalidar o zero na conta de par e impar
        if x % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Números Par digitados: {par}')
print(f'Número impar digitados: {impar} ')
print('Acabou')