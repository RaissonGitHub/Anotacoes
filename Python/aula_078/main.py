# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O pyhton conhece a pasta onde o __main__ está e as pasta
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por 
# padrão
# O pyhton conhece todos os módulos e pacotes presentes 
# nos caminho de sys.path

import sys

import aula078_m

print('Este módulo se chama', __name__)

print(*sys.path,sep='\n')
