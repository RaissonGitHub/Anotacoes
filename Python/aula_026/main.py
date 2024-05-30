"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo,valor,identidade)
id = Identidade
"""

v1 = 'a'
v2 = 'a'
v3 = 'ba'

print(id(v1))
print(id(v2))
print(id(v3))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')

else:
    print('Não faça algo')
print(passou_no_if, passou_no_if is None)

"""
is e is not verificam identidade de objetos, enquanto == e != verificam 
igualdade de valores. Usar is e is not é vantajoso quando se deseja 
verificar se dois objetos referenciam exatamente o mesmo objeto na memória, 
não apenas se possuem valores iguais. É útil, por exemplo, ao trabalhar com 
o objeto None ou ao verificar se duas variáveis referenciam o mesmo objeto 
mutável.
"""