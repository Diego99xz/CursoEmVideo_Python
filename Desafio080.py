print('====== DESAFIO 080 ======')

# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção(sem usar o sort())
# No final, mostre a lista ordenada na tela.

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    
    if not numeros or num > numeros[-1]:  # Se a lista estiver vazia ou num for maior que o último valor
        numeros.append(num)
        pos = len(numeros) - 1
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                break
            pos += 1
    
    print(f"Número {num} adicionado na posição {pos}.")

print("Lista ordenada:", numeros)