# Operadores lógicos
# and   or   not

# and - Todas as condições precisam ser 
# verdadeiras.
# Se qualquer valor for falso,
# a expressão inteira será avaliada naqule valor
# São considerados falsy 
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida : 
    print('Entrar')
else : 
    print('Sair')

# Avaliação de curto circuito
print(True and True and True)
print(True and False and True)