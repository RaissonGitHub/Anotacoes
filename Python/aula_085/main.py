# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradas são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f"O seu resultado foi {resultado}")
        print("Ok, aogra você foi decorada.")
        return resultado

    return interna

@criar_funcao
# Estou passando inverte_string para criar_funcao
# inverte_string se transformara na funcao interna
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")



invertida = inverte_string("Ricardo")
print(invertida)


