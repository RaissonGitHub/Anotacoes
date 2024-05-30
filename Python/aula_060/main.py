# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'sobrenome'
pessoa['nome'] = 'Ricardo'
pessoa[chave] = 'Algusto'

print(pessoa)
print(pessoa[chave])
#del pessoa['sobrenome'] # excluir a chave
print(pessoa)

# retorna o segundo argumento ou None se a chave nao existe
print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
