print('====== DESAFIO 053 ======')

#Crie um programa que leia um frase qualquer e diga se ela é polindromo, desonsiderando os espaços

frase = str(input('Informe uma frase: '))

frase = frase.replace(' ','').lower()
fraseRev = frase[::-1]

if frase == fraseRev:
    print('Essa frase é Palíndromo')
    print(f'Normal: {frase}')
    print(f'De trás pra frente: {fraseRev}')
