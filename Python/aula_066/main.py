# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. OU seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {"nome": "Luiz", "sobrenome": "miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Fernando", "sobrenome": "Silva"},
    {"nome": "Ana", "sobrenome": "Machado"},
]


# def ordena(item):

#     return item["nome"]


lista.sort(key=lambda item: item["nome"])

# for item in lista:
#     print(item)

# Transformando em lambda
    
def executa(funcao, *args):
    return funcao(*args)


# def soma(x,y):
#     return x + y

soma = executa(
    lambda x,y: x + y,
    1,2
)
print(soma)

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

duplica =executa(
    lambda m: lambda n: n*m,
    2
)
# print(duplica(2))