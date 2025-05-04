def aumentar(n, percent, f):
    porcentagem = n*(percent/100)
    valor = n + porcentagem
    if f:
        return f'R$ {valor:.2f}'
    else: 
        return valor

def diminuir(n, percent, f):
    porcentagem = n*(percent/100)
    valor =  n - porcentagem
    if f:
        return f'R$ {valor:.2f}'
    else: 
        return valor

def dobro(n, f):
    valor = n * 2
    if f:
        return f'R$ {valor:.2f}'
    else: 
        return valor

def metade(n, f):
    valor =  n / 2
    if f:
        return f'R$ {valor:.2f}'
    else: 
        return valor

def moeda(n):
    return f'R$ {n:.2f}'

def resumo(n, a, r):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{r}% de redução: \t{diminuir(n, r,True)}')
