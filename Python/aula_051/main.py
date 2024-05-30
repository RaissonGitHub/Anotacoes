"""
Escopo de funções em Python
Escopo siginifica o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

z = 3
y = 2


def escopo():
    x = 1
    def outra_funcao():
        z = 10
        print(x,y,z)
    outra_funcao()


print(y)
escopo()
print(z)
# print(x) # x is not defined
