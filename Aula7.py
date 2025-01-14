print('====== Aula 007 ======')

# Operadores Aritméticos
# 5+2 == 7 adição
# 5-2 == 3 subtração
# 5*2 == 10 Multiplicação
# 5/2 == 2.5 Divisão
# 5**2 == 25 Potência
# 5//2 == 2 Divisão Inteira
# 5%2 == 1 Resto da Divisão

# Ordem de Precedência
# 1 ()
# 2 **
# 3 * / // % Faz quem aparecer primeiro
# 4 + -

# Exemplo
# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4) ** 2 = 243

#calculando raiz Quadrada
print(81**(1/2))
#potência
print(4**3)
#portência
print(pow(4,3))

#printando igual 20 vezes
print('='*20)

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

print('='*30)
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2

print('A soma é {}\no produto é {}\nA divisão é {:.3f}'.format(s, m, d))
print('A Divisão inteira {}\nA potência {}'.format(di, p))
