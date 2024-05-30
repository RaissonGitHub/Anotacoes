# Métodos úteis dos dicionários em Python

# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa ( shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro

import copy

pessoa = {"nome": "Ricardo", "sobrenome": "Algusto", "l1": [1, 2, 3]}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
pessoa.setdefault("idade", 0)

# diferente de pessoa2 = pessoa
# shadow copy, copia os itens imutáveis e os mutaveis ainda sao afetados por outros dicionarios
pessoa2 = pessoa.copy()

# copia profunda, outro dicionario nao afetara pessoa3
pessoa3 = copy.deepcopy(pessoa)


# valores apontam para lugares diferentes na memoria, idade em pessoa 0, idade em pessoa2 18
pessoa2["idade"] = 18
# valores apontam para o mesmo lugar na memoria, l1 [1,55,3] nas duas pessoas
pessoa2["l1"][1] = 55
print(pessoa)
print(pessoa2)
print(pessoa3)

print(pessoa.get('cpf', 'Não existe'))

nome = pessoa.pop('nome')
print(nome)
print(pessoa)


ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)


pessoa.update({
    'sobrenome': 'Oliveira',
    'cor': 'Azul'
})
print(pessoa)

tupla = (('sobrenome', 'outro valor'), ('idade', 16))
pessoa.update(tupla)
print(pessoa)