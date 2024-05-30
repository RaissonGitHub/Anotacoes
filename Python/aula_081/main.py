# from sys import path

# import aula_081_package.modulo
# from aula_081_package import modulo 
# from aula_081_package.modulo import* 

# from aula_081_package.modulo import soma

# print(*path, sep='\n')
# print(soma(1,1))
# print(aula_081_package.modulo.soma(1,2))
# print(modulo.soma(1,2))
# print(variavel)
# print(nova_variavel)
from aula_081_package.modulo import soma

print(__name__)

import aula_081_package

print(aula_081_package.dobra(2))
