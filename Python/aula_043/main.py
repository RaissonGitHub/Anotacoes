# split e join com list e str
# split - divide uma string
# join - une uma string

frase1 = 'Olha só que, coisa interessante'
lista_palavras = frase1.split()
# se não informar nenhum argumento, ele separa pelos espaços
print(lista_palavras)

quebra_virgula = frase1.split(',')
print(quebra_virgula) # duas frases 

espacos = '           Olha só que     , coisa interessante          '
outra_lista = espacos.split(',')

for i, frase in enumerate(quebra_virgula):
    print(quebra_virgula[i].strip()) # remove os espaços do fim e começo
    # print(quebra_virgula[i].lstrip()) # remove os espaços do começo
    # print(quebra_virgula[i].rstrip()) # remove os espaços do fim 


lista_frases = []
for i, frase in enumerate(outra_lista):
    lista_frases.append(outra_lista[i].strip())
print(outra_lista)
print(lista_frases)

# Join

uma_frase = '-'.join('abc') # a-b-c
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)