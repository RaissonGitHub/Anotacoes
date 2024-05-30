from functools import partial

# map - para mapear dados


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


def aumentar_porcentagem(valor, porcento):
    return round(valor * porcento, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcento = 1.1
)

# novos_produtos = [
#     {**p,
#      'preco': aumentar_dez_porcento(p['preco'])}
#      for p in produtos
# ]

def muda_preco(produto):
    return{
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

# primeiro param é uma funcao o segundo um iteravel
novos_produtos = list(map(muda_preco,produtos))

print_iter(produtos)
print_iter(novos_produtos)