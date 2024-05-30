# Enumerate - enumerar iteráveis (índices)
#  [(0, 'Maria'), (1, 'João'), (2, 'José'), (3, 'Claudio')]
# Cria uma tupla com o índice e o item
lista = ['Maria','João','José']
lista.append('Claudio')

lista_enumerada = list(enumerate(lista))
print((lista_enumerada))
print('-'*50)

for indice in lista_enumerada :
    print(indice)

# for indice in lista_enumerada :
#     print(indice)
    
print('-'*50)

# Se fizer outro for lista_enumerada estará vazia e não executará o for, pois o enumerete esgotou seu valor
# Mais produtivo fazer enumerate() em todo novo for

for item in enumerate(lista) :
    print(item)
print('Outra vez')
for item in enumerate(lista) :
    print(item)
# Mais facil e tendo controle sobre o índice e conteúdo
for indice, nome in enumerate(lista):
    print(f'Indice: {indice}, nome: {nome}')

print('-'*50)

# Se quiser imprimir individualmente
for tupla_enumerada in enumerate(lista) :
    print('For da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
