# Try, except, else, finally

# tenta executar o código
# se der certo, executa o código
try:
    a = 1
    b = 0
    c = a/b
    print('linha 1')
    print(c)
    print('linha 2')

# se der erro, executa o códigoa execpt
except ZeroDivisionError: 
    print('Dividiu por zero')
except NameError: 
    print('Erro de nome, algo não está definido')
# para mais de um erro
# capturar erro com as
except (TypeError,IndexError) as error:
    print('Erro de tipo ou índice')
    print('Msg',error)
    print('Nome:',error.__class__.__name__)
else:
    print('Não deu erro')
# sempre é executado independente se houve erro
finally:
    print('Executado')
print('Continuar')