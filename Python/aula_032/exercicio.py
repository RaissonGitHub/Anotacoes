frase = (
    "O Python é uma linguagem de programação "
    "multiparadigma. "
    "Python foi criado por Guidovan Rossoum."
)

letra_mais_repitida = ""
mais_apareceu = 0
i = 0
while i < len(frase):
    letra_atual = frase[i]
    apareceu = frase.count(letra_atual)
    if apareceu > mais_apareceu and letra_atual != " ":
        letra_mais_repitida = letra_atual
        mais_apareceu = frase.count(letra_atual)
    i += 1
print(f"Letra que mais apareceu: {letra_mais_repitida} que apareceu: {mais_apareceu} vezes")
