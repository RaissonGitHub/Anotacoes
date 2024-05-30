# Para recarregar um módulo mais de uma vez
import importlib

import aula078_m

print(aula078_m.variavel)

for i in range(10):
    # use reload para recarregar o módulo
    # caso contrário será carregado uma única vez
    importlib.reload(aula078_m)
    print(i)

print('Fim')