# Listas em python

# Tipo list - Mutável
# Métodos úteis: append, insert, pop, del, clear, extend +
# Create, Read, Update, Delete
# lista[i] (CRUD)
"""
append - Adiciona ao final da lista
insert - Adiciona item no indice informado
pop - remove ao final ou do indice informado
del - apaga um indice
clear - limpa uma lista
extend - extende uma lista
+ - concatena listas
"""

lista = list() # menos convencional
lista = [123, 'ola', True, [] ]
#         0     1      2    3
print(lista)
print(lista[1])
lista[1] = 'mundo'
print(lista[1])
print(lista)
del lista[2]
# lista = [123, 'ola', [] ]
#          0      1     2
print(lista)
lista.append(True) # adiciona ao final da lista
print(lista)
ultimo = lista.pop() # remove do final da lista e armazena
lista.append(4534545)
lista.append(453)
print(lista)
lista.pop(-2) # removendo de um indice especifico
print(lista)
# lista.clear()
print(lista)
lista.insert(2,False)
print(lista)


lista_a = [1,2,3,4]
lista_b = [5,6,7,8]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # meche na lista a
print(lista_c)
print(lista_a)
uma_lista = lista_b.copy() # copia o conteudo da lista_b
# uma_lista = lista_b -> apontam para o mesmo endereço de memoria, se alterar lista_b altera uma_lista