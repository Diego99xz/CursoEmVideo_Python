print('====== DESAFIO 073 ======')

#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação. Depois Mostre:
# A)Apenas os 5 primeiros colocados.
# B)Os últimos 4 colocados da tabela.
# C)Uma lista com os times em ordem alfabética.
# D)Em que posição na tabela está o time da Chapecoense.

tabela = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional',
         'São Paulo','Corinthians','Bahia','Cruzeiro','Vasco',
         'Vitória','Atlético-MG','Fluminense','Grêmio','Chapecoense',
         'Bragantino','Atlético-PR','Criciúma','Atlético-GO','Cuiabá')

print(30*'=-')
print(f'Os 5 Primeiros colocados:\n{tabela[:6]}')
print(30*'=-')
print(f'Os 4 Últimos colocados:\n{tabela[-4:]}')
print(30*'=-')
print(f'Tabela em Ordem alfabética:\n{sorted(tabela)}')
print(30*'=-')
print(f'Posição do Chapeconse na Tabela:\n{tabela.index('Chapecoense')}º')
print(30*'=-')