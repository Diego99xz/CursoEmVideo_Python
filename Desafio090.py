print('====== DESAFIO 090 ======')

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['media']= float(input(f'Média de {boletim['nome']}: '))

if boletim['media'] >=6:
    boletim['situacao'] = 'Aprovado'
else:
    boletim['situacao'] = 'Reprovado'

print('-='*20)
print(f'Nome é igual a {boletim['nome']}')
print(f'Média é igual a {boletim['media']}')
print(f'Situação é igual a {boletim['situacao']}')