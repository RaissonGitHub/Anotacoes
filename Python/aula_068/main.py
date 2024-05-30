# List comprehension em Python
# List comprehension 'e uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

lista = [numero for numero in range(10)]
print(lista)
print('')

lista = [numero * 2 for numero in range(10)]
print(lista)
print('')

# Mapeamento de dados em list comprehension
produtos = [
    {"nome": "p1", "preco": 20.00},
    {"nome": "p2", "preco": 30.00},
    {"nome": "p3", "preco": 10.00},
]

novos_produtos = [
    # {'nome':produto['nome'],'preco':produto['preco']}
    # ternario com mapeamento
    (
        {**produto, "preco": produto["preco"] * 1.05}
        if produto["preco"] > 20
        else {**produto}
    )
    for produto in produtos
]

print(*novos_produtos, sep="\n")
print('')

# Filtro de dados

lista = [n for n in range(10) if n < 5]
print(lista)
print('')


novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20 else {**produto}
    for produto in produtos
    # Pode incluir ou nao um elemento
    if produto["preco"] >= 20 and produto["preco"] * 1.05 > 20
]
print(novos_produtos)
print('')

outra_lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)   
]
print(outra_lista)
print('')
outra_lista = [
    [x for y in range(3)]
    for x in range(3)
]

print(outra_lista)