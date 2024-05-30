# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


produtos = [
    {"nome": "Produto 3", "preco": 130.55},
    {"nome": "Produto 4", "preco": 10.03},
    {"nome": "Produto 1", "preco": 10.0},
    {"nome": "Produto 2", "preco": 220.20},
    {"nome": "Produto 5", "preco": 55.12},
]

# novos_produtos = [
#     p 
#     for p in produtos
#     if p['preco'] > 100
# ]

# primeiro param é uma funcao e o segundo um iteravel
novos_produtos = filter(
    lambda p: p['preco'] > 100,
    produtos
)

print_iter(novos_produtos)