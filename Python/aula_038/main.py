# Introdução ao desempacotamento + tuples (tuplas)

nomes = ["Maria", "Ana", "José"]
nome1, nome2, nome3 = nomes
print(nome2)


# Para pegar um valor e descartar o resto
# _ é uma váriavel com o resto da lista, mas por convensão, quer dizer que ela não será utilizada

_, nome2 , *_, = ["Ana", "João", "José"]
print(nome2)