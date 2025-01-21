print('====== DESAFIO 037 ======')

#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 - Biário
# 2 - Octal
# 3 - Hexadecimal

n = int(input('Informe um número: '))

opcao = int(input('1 - Binário\n 2 - Octal \n 3 - Hexadecimal\n Escolha a Conversão: '))

if opcao == 1:
    binario = bin(n)
    print(f'Número Binário: {binario}')
elif opcao == 2:
    octal = oct(n)
    print(f'Número Octal: {octal}')
elif opcao == 3:
    hexadecimal = hex(n)
    print(f'Número Hexadecimal: {hexadecimal}')
else:
    print('Opção inválida!')