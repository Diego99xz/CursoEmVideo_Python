print('====== DESAFIO 069 ======')

#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
'''
A)Quantas pessoas tem mais de 18 anos.
B)Quantos homens foram cadastrados.
C)Quantas mulheres tem menos de 20 anos.
'''
n = 1
continuar = True
maior_idade = 0
homens = 0
mulher_menor20 = 0
while continuar == True:
    print(f'{n}º Pessoa')
    idade = int(input('Qual a idade: '))
    sexo = str(input('[M]Masculino - [F]Feminino\nInforme o sexo: '))
    sexo = sexo.upper() 

    if idade > 18:
        maior_idade += 1
    
    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulher_menor20 += 1

    opcao = str(input('[S]Sim - [N]Não\nDeseja continuar ? '))
    opcao = opcao.upper()

    if opcao == 'N':
        break

    n += 1

print(f'Pessoas com mais de 18anos: {maior_idade}')
print(f'Quantidade de homens {homens}')
print(f'Mulheres com menos de 20 anos: {mulher_menor20}')