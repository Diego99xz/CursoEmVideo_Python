def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
        
def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite um número inteiro válido.')