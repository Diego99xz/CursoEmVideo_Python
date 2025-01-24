print('====== DESAFIO 056 ======')

#Desenvolva um progra que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

lista_nomes = []
lista_idades = []
lista_sexo = []
for i in range(1, 4+1):
    print(f'Informe os Dados da {i}º Pessoa')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    print('Qual o sexo ?\n[1]-Masculino\n[2]-Feminino')
    sexo = int(input('Digite o número referente ao sexo: '))
    print('---------------------------------------------')
    if sexo == 1 or sexo == 2:
        lista_nomes.append(nome)
        lista_idades.append(idade)
        lista_sexo.append(sexo)
    else:
        print('Número de Sexo errado!')
        print('Programa Encerrado!')
        break

media = (lista_idades[0] + lista_idades[1] + lista_idades[2]+ lista_idades[3]+ lista_idades[4]) / len(lista_idades)
mais_velho = max(lista_idades)
mais_velho = lista_nomes
