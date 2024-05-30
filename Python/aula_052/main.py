"""
Escopo de funções em Python
Escopo siginifica o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
A palavra global permite a manipulação de variáveis externas
dentro das funções, podendo alterar seus valores.
Não é uma boa prática usar global.
"""

x = 1
z = 3
y = 2


def escopo():
    global x
    x = 2
    def outra_funcao():
        global x
        z = 10
        x = 3
        print(x,y,z)
    print(x)
    outra_funcao()


print(x)
escopo()
print(x)

