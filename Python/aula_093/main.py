# reduce - faz a redução de um terável em um valor
from functools import reduce

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

# primeiro param é uma funcao com um acumulador
# o segundo é um iteravel
# o terceiro é o valor inicial
total = reduce(
    lambda acumulador, p: acumulador + p['preco'],
    produtos,
    0
)

# total = 0
# for produto in produtos:
#     total += produto["preco"]
print(total)