print('====== Aula 011 ======')

#Aula Extra
#Cores no terminal

#código para colocar cor
#\033[Estilo da fonte;cor do texto;Cor de fundo m

#Código estilo da fonte
# 0 - None
# 1 - Bold
# 4 - Underline
# 7 - Negative

#Código cor de texto
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Ciano
# 37 - Cinza

#Código cor de fundo
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Roxo
# 46 - Ciano
# 47 - Cinza

'''
Exemplos:
\033[0;30;41:m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
'''

#Exemplo
print('\033[1;31;43mOlá, Mundo!\033[m')

a = 3
b = 5
print('OS Valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Diego'
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['vermelho'],nome,cores['limpa']))