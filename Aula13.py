print('====== Aula 013 ======')

#Estrutura de repetições 

#Contagem
for c in range(0,6):
    print(c)
print('fim')

#Contagem Regressiva
for c in range(6, 0, -1):
    print(c)
print('fim')

#Contagem com pulo
for c in range(0, 6, 2):
    print(c)
print('fim')

#Contando até o número pedido
n = int(input('Digite um número: '))
for c in range(0, n+1):#o +1 faz com que conte até o numero informado
    print(c)
print('FIM')

#Contando determinando inicio, fim e tamanho do passo
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p ):
    print(c)
print('FIM')

#Somando os valores com for 
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    #s = s + n
    s += n
print(f'O Somatório de todos os valores foi {s}')