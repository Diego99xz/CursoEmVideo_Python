print('====== DESAFIO 110 ======')

# adicione ao módulo moeda.py criado nos desafios anteriores, uma funçãp chamada resumo()
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from pacote import moeda

p = float(input('Digite o Preço: R$ '))
moeda.resumo(p, 80, 35)