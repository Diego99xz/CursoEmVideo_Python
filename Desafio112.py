print('====== DESAFIO 112 ======')

# Dentro do pacote utilidadesCeV qie croa,ps mp desafop 111, temos um módulo
# chamado dados. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar
# como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários

from utilidadesCeV import moeda
from utilidadesCeV import dados

p = dados.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 12)
