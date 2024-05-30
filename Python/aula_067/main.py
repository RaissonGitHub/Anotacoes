# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

a, b = pessoa
print(a, b)
print("")
a, b = pessoa.values()
print(a, b)
print("")

a, b = pessoa.items()
print(a, b)
print("")

(a1, a2), (b) = pessoa.items()
print(a1, a2, b)
print("")

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2, b1, b2)
print("")

# Mesmo que
# for chave,valor in pessoa.items():
#     print(chave,valor)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

dados_pessoa = {"idade": 16, "altura": 1.6}

# Juntar um dicionario

pessoa_completa = {**pessoa, "chave": 1}
print(pessoa_completa)
print("")

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
print("")


def mostro_argumetnos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS:", args)
    print(f"NOMEADOS {kwargs}")
    for chave, valor in kwargs.items():
        print(chave,valor)
    print("")


mostro_argumetnos_nomeados(nome="Joana", qlq=123)
mostro_argumetnos_nomeados(1, 2, True)
mostro_argumetnos_nomeados(1, 2, True, nome="Joana", qlq=123)

mostro_argumetnos_nomeados(**pessoa_completa)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumetnos_nomeados(**configuracoes)
