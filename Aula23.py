print('====== Aula 023 ======')

# Tratamento de erros

# try é para tentar a operação
try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
# except é o que apresentará se falhar
    print('Infelizmente tivemos um problema :( ')

print(f'O resultado é {r}')
