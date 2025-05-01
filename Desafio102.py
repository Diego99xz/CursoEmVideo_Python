print('====== DESAFIO 102 ======')

# Crie um programa que tenha uma função fatorial() que receba dois parâmentros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
    """
    -> Clacula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Ovalor do Fatorial de um número num
    """
    f = 1
    if show:
        print(f'Calculo do fatorial de {num}:')
        for c in range(num, 0, -1):
            f *= c
            if num != c: 
                print(f'{num} X {c} = {f}')
        return f'Resultado Final: {f}'
    else:
        for c in range(num, 0, -1):
            f *= c 
        return f'O resultado do Fatorial de {num} é {f}'



print(fatorial(5, True))
help(fatorial)