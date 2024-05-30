# Dicitionary comprehension e Set comprehension

produto = {
    'nome': 'Caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave: valor.upper()
    # verificar se é str
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    # Se nao quiser incluir alguma chave e valor
    # if chave != 'categoria'
}

print(dc)

# set
se = {
        i**2
        for i in range(10)
      }
print(se)