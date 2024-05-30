# Exercico - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

def zipper(lista1, lista2):
    if len(lista1) > len(lista2):
        lista1, lista2 = lista2, lista1
    resultado = [(cidade, lista2[i]) for i, cidade in enumerate(lista1)]

    return resultado


cidades = ["Salvador", "Ubatuba", "Belo Horizonte"]
estados = ["BA", "SP", "MG", "RJ"]

# print(zipper(estados, cidades))
# print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='Sem Cidade')))
