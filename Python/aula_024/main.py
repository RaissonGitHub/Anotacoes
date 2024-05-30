"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Digite um número: ')

try:
    print('STR:', numero)
    numero_float = float(numero) # se nao for um número vai para except
    print('FLOAT:',numero_float)
    print(f'O dobro de {numero} é {numero_float*2}')
except :
    print('Isoo não é um número')