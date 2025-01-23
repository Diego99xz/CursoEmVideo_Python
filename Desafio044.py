print('====== DESAFIO 044 ======')

#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: Preço normal
#3x ou mais no cartão: 20% de Juros

preco = float(input('Informe o preço do produto: '))

print('Formas de Pagamento:\n[1] Dinheiro\n[2] Cheque\n[3] Cartão 1x\n[4] Cartão em 2x\n[5] Cartão em 3x')
opcao = int(input('Escolha o número da opção de pagamento: '))

if opcao == 1:
    desconto = preco * (10/100)
    novo_preco = preco - desconto
    print(f'Produto no Dinheiro Tem 10% Desconto R$ {novo_preco:.2f}')
elif opcao == 2:
    desconto = preco * (10/100)
    novo_preco = preco - desconto
    print(f'Produto no cheque Tem 10% Desconto R$ {novo_preco:.2f}')
elif opcao == 3:
    desconto = preco * (5/100)
    novo_preco = preco - desconto
    print(f'Produto no Cartão em 1x Tem 10% Desconto R$ {novo_preco:.2f}')
elif opcao == 4:
    print(f'Produto no Cartão em 2x R$ {preco:.2f}')
elif opcao == 5:
    juros = preco * (20/100)
    novo_preco = preco + juros
    print(f'Produto no Cartão em 3x Tem 20% Juros R$ {novo_preco:.2f}')
else:
    print('Forma de pagamento inválida!')