"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, ovalor padrão será 
usado.
"""


def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} + {y=} + {z=} = ", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)


soma(1, 2)
soma(1, 2, 0)
soma(y=1, x=2, z=0)
