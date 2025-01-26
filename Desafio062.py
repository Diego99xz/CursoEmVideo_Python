print('====== DESAFIO 062 ======')

#Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. Oprograma encerra quando ele disser que quer mostrar 0 termos

n1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
fim = 10
c = 0
while c < fim:
    print(n1)
    n1 = n1 + r
    c += 1
    
    if c == fim:
        fim = int(input('Você quer mostar mais quantos termos? '))
        fim += 10
print('Programa encerrado!')