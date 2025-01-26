print('====== DESAFIO 057 ======')

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#caso esteja errado, peça a digitação novamente até ter um valor correto.

valido = 'N'

while valido == 'N':
    sexo = str(input('Informe o seu sexo com letra incial:\nM ou F:' ))
    sexo = sexo.upper()
    if sexo == 'M' or sexo == 'F':
        valido = 'S'

print('Obrigado pela Informação!')