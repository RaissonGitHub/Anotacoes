"""
Dicionarios em Python (tipo dict)
Dicionarios sao estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imtáveis 
como: str,int float, bool,tuple,etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para
criar dicionarios.
Imutáveis: str,int, float, bool, tuple
Mutável: dict, list 
"""
# pessoa = dict(nome= "luiz otavio",sobrenome="miranda")
pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 18,
    "altura": 1.8,
    "enderecos": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 132},
    ],
}
print(type(pessoa))
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])