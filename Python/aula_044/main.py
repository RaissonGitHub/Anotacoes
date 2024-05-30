# Lista de listas e seus índices

salas = [
    #   0        1
    ['Maria','Helena'], # 0
    #  0
    ['Eliana'], # 1
    # 0         1         2              3
    ['Luiz', 'Gustavo', 'Vitor' ], # 2
    #[(0,10,20,30,40)]
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
# print(salas[3][0][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)


