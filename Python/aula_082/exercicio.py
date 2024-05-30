# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy

# Ordene os produtos por preço crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy

import copy

produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]
novos_produtos = [
        {**i, 'preco': i['preco'] * 1.1
        }
        for i in copy.deepcopy(produtos)
    ]



produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda x: x["nome"], reverse=True
)

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda x: x["preco"])

# for i,j in enumerate(produtos):
#     print(j['nome'], j['preco'])

# print(novos_produtos)

# for i,j in enumerate(novos_produtos):
#     print(j['nome'], j['preco'])



# for i,j in enumerate(produtos_ordenados_por_nome):
#     print(j['nome'], j['preco'])

for i, j in enumerate(produtos_ordenados_por_preco):
    print(j["nome"], j["preco"])
