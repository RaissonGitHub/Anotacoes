# Closure e funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'

    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(bom_dia('Ricardo'))
for i in ['Maria', 'João', 'Luiz']:
    print(bom_dia(i))
    print(boa_noite(i))