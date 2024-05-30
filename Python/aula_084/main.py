# Variaveis livres + nonlocal (locals, globals)


def fora(x):
    a = x
    # a é uma variavel livre
    # ela não pode ser alterada dentro da funcao dentro
    
    def dentro():
        return a

    return dentro

dentro1 = fora(10)
print(dentro1())

def concatenar(string_inicial):
    # valor_final é uma variavel livre
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        # informando a variavel como nonlocal é possivel altera-la na funcao
        nonlocal valor_final
        # se nao houver nonlocal ocorrerá um erro
        valor_final += valor_a_concatenar
        return valor_final

    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
