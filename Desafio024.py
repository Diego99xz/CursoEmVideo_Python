print('====== DESAFIO 024 ======')

#Crie um progra que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Informe a cidade: '))
cidade = cidade.upper()
print(cidade[:5] == 'SANTO')
