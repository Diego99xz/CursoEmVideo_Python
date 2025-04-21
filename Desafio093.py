print('====== DESAFIO 093 ======')

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
tot = 0

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i+ 1} ? ')))
    tot += gols[i]
jogador['gols'] = gols
jogador['total'] = tot
print('-='*20)
print(jogador)
print('-='*20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*20)
print(f'O jogador {jogador['nome']} jogou {partidas}.')

for i in range(0, partidas):
    print(f'    => Na partida {i+1}, fez {jogador['gols'][i]} gols.')