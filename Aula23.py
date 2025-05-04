print('====== Aula 023 ======')

# Tratamento de erros

# try é para tentar a operação
try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except:
# # except é o que apresentará se falhar
#     print('Infelizmente tivemos um problema :( ')
except (ValueError, TypeError) as erro:
    print('Tivemos um problema com os tipos de dados que você digitou.')
    print(f'Problema encontrado foi {erro.__class__}')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
# Se der certo faça...    
    print(f'O resultado é {r:.1f}')

finally:
# Idependente se deu certo ou erro vai ocorrer
    print('Volte sempre! Muito obrigado!')