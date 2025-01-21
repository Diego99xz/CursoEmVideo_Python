print('====== DESAFIO 036 ======')

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar "o valor da casa", o "Salário" do comprador e em "quantos anos" ele vai pgar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

vl_financiamento = float(input('Valor d R$: '))
salario = float(input('Informe seu salário: '))
anos = int(input('Prazo de pagamentos em Anos: '))

pmt = salario * 0.3
qtd_parcela = 12 * anos
vl_parcela = vl_financiamento / qtd_parcela

if pmt >= vl_parcela:
    print('\nSeu Financiamento foi Aprovado!')
    print(f'Valor do Financiamento R$ {vl_financiamento:.2f}')
    print(f'Quantidade de Parcelas: {qtd_parcela}X')
    print(f'Valor da Parcela R$: {vl_parcela:.2f}')
else:
    print('\nSeu Financiamento foi Negado!')
    print('Você ultrapassou sua PMT "Parcela máxima permitida"')
    print(f'O valor da sua parcela deve ser menor que R$ {pmt:.2f}')
