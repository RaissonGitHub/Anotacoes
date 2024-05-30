# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {"nome": "Ana", "nota": "A"},
    {"nome": "Bia", "nota": "D"},
    {"nome": "Dida", "nota": "C"},
    {"nome": "Xica", "nota": "A"},
    {"nome": "Otávio", "nota": "C"},
    {"nome": "Nita", "nota": "B"},
]

def ordena(aluno):
    return aluno['nota']

alunos.sort(key=ordena)

grupos = groupby(alunos,key=ordena)

# CUIDADO! se algum 'a' não estiver em ordem será considerado outro elemento
# alunos = ["a", "a", "a", "a", "b", "c", "a"]
# alunos.sort()
# grupos = groupby(alunos)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
