# Sets - Conjuntos em Pyhton (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(inerável) pi {1,2,3}
s1 = set()  # vazio
s1 = {"Luiz", 1, 2, 3}  # com dados
print(type(s1))
print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# Seus valores serão sempre únicos;
# - nao acietam valores mútaveis;
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

s1 = {1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1}
# elemina valores duplicados
print(s1)

# Métodos úties:
# add, update, clear, discard

s1 = set()
s1.add("Luiz")
s1.add(1)
print(s1)
s1.update(("Olá mundo", 1, 2, 3))
print(s1)
# s1.clear()
s1.discard("Olá mundo")
print(s1)

# Operadores úties:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^- Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # {1, 2, 3, 4}

s3 = s1 & s2  # {2,3}

s3 = s1 - s2  # {1}
s3 = s2 - s1  # {4}

s3 = s1 ^ s2  # {1,4}

print(s3)
