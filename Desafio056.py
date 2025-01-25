print('====== DESAFIO 056 ======')

#Desenvolva um progra que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

soma_idades=0
old_man = {"nome": "", "idade": 0}
mulheres_menos_20 = 0

for i in range(1, 5+1):
    print(f'Informações da {i}º Pessoa')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M]-Masculino\n[F]-Feminino\nInforme a letra do seu sexo: '))
    sexo = sexo.upper()

    soma_idades = soma_idades + idade

    if sexo ==  'M' and idade > old_man["idade"]:
        old_man["nome"] = nome
        old_man["idade"] = idade

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media = soma_idades/5

print(f'A Média de didade do grupo é {media}')
print(f'O Homem mais velho é o {old_man["nome"]}')
print(f'Quantidade de mulheres com menos de 20 anos:  {mulheres_menos_20}')