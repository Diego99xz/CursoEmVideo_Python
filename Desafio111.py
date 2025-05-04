print('====== DESAFIO 111 ======')

# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dados.
# Transfira todas as funções utilizdas nos desafios 107, 108 e 109
# para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 12)
