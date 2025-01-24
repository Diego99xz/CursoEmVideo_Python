print('====== DESAFIO 054 ======')

#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

menor = 0
maior = 0
for i in range(1,7+1):
    ano = int(input(f'Informe o Ano de nascimento da {i}º Pessoa: '))
    idade = 2025 - ano

    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'Pessoas Maior de idade: {maior}')
print(f'Pessoas menor de idade: {menor}')
    