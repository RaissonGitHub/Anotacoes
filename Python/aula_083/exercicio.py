# Exercicio - Adiando execução de funções

def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao,x):
    def funcao_criada(y):
        return funcao(x, y)
    return funcao_criada

soma_com_cinco = criar_funcao(soma,5)
multiplica_por_dez = criar_funcao(multiplica,10)

print(soma_com_cinco(1))
print(multiplica_por_dez(2))