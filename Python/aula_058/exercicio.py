"""
Exercicos
Crie funcoes que duplicam, triplicam e quadruplicam
o número recebido como parametro
"""
def multplicar(n):
    def mult(i):
        return n * i
    return mult

duplicar = multplicar(2)
print(duplicar(3))