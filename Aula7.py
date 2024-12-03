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

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end=' ')
print('a divisão inteira {} e a potência {}'.format(di, e))

#como calcular raiz quadrada
# 5**(1/2)