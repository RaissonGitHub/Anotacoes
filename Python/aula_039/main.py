# Tuples (tuplas)
# Uma lista imutável

# Uma lista sem []
nomes = 'Maria', 'Claudia', 'Joana'
# poderia ser assim também:  nomes = ('Maria', 'Claudia', 'Joana')

_, _, nome3, *_ = nomes
print(nomes)
print(nome3)

# nomes[0] = True # Erro!


# Convertendo uma lista para tupla

lista = [1,2,3,4]
print(type(lista))
tupla = tuple(lista)
print(type(tupla))