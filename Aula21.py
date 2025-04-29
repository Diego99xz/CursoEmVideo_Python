print('====== Aula 021 ======')

# Interactive Help
# Docstrings
# Argumentos opcionais
# Escopo de variáveis
# Retorno de resultados


# Interactive Help: chama  no código e interage no console para entender manual do python
#help()
#ou
#help(print)

#---------------------------------------------------------------
# Docstrings: maneira de Documentar uma função ou programa.
def contador(i, f, p):
    """"
    -> faz um contagem e mostra na tela.
    :param i: início de contagem
    :param f: fim da semana
    :param p: passo de contagem
    :return: sem retorno
    Função criada por Diego Melo
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

contador(2,10,2)

help(contador) # Mostra minha Docstring

#--------------------------------------------------------------------
# Argumentos opcionais, adicionando zero  nos parametros a função pode passar
#  3,2, 1 ou zero paramentros para ser chamada

def somar(a =0, b=0, c=0):
    s= a+ b+ c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar()

#--------------------------------------------------------------------
# Escopo de variáveis
# x só está declarado dentro da função então ele não existe fora da função
# n é uma variavel global que existe em todo escopo.
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x} ')

# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()

#--------------------------------------------------------------------
# Retorno de valores
def somar(a =0, b=0, c=0):
    s= a+ b+ c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar()
print(f'Os resultados foram {r1}, {r2} e {r3}')
#--------------------------------------------------------------------

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

#--------------------------------------------------------------------
def par(n=0):
    if n % 2 ==0:
        return True
    else: 
        return False
    
num  = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')