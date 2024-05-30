import sys
# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # item __iter__ e __next__
# ou 
# iterator = iterable.__iter__() 
print(next(iterator))
print(next(iterator))

# está na memória
lista = [n for n in range(10000)]

# função que pausa
# não tem tamanho
# não tem índice
# está esperando ser executado
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))