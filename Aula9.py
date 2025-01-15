print('====== Aula 009 ======')

#Tecnica de Fatiamento
frase = 'Curso em Video Python'
print(frase[9])#capturando uma Letra
print(frase[9:14])#capturando uma cadeia de caracter
print(frase[9:21:2])#capturando uma cadeia de caracter saltando de 2 em 2
print(frase[:5])#capturando o inicio até o caracter 5
print(frase[15:])#capturando do caracter 15 até o final
print(frase[9::3])#captura do caracter 9 até o final saltando de 3 em 3
print(len(frase))#conta a quantidade de caracter da string
print(frase.count('o'))#conta quantas letras 'o' tem na frase
print(frase.count('o',0,13))#conta quantas letras 'o' tem na frase entre o intervalo de caracter 0 e 13
print(frase.find('deo'))#pesquisa quando começou 'deo' na frase.
print(frase.find('Android'))#Quando retorna um valor que não existe ele retorna -1
print('Curso' in frase)#Existe 'Curso' em frase ? valor bool

#Transformação
frase.replace('Python', 'Android')#Substitui 'Python' por 'Android'
frase.upper()#coloca tudo em maiusculo
frase.lower()#coloca tudo em minusculo
frase.capitalize()#Coloca tudo em minusculo e a primeira letra da frase e maiusculo
frase.title()#Coloca toda primeira letra de uma palavra em maiusculo e o restante em minusculo
frase2 = '   Aprenda Python   '
frase2.strip()#Remove espaço no inicio e no fim da frase
frase2.rstrip()#Remove espaço no fim "Direita" de R right
frase2.lstrip()#Remove espaço no inicio "esquerda" de L left

#Divisão
frase.split()#divide a frase pelo delimitador espaço

#Junção
'-'.join(frase)#Junta a lista de palavras frase em uma só com delimitador -

