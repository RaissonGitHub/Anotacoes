"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá mundo'

print(variavel[4:]) # pegar do 4 até o fim
print(variavel[0:5]) # pegar do 0 até o 5
print(variavel[-8:3]) # pegar do -8 até o 3
print(len(variavel)) # tamanho da str


# começa do 0 e vai até o comprimento da str pulando de 2 em 2
print(variavel[0:len(variavel):2])

# com -1
print(variavel[::-1]) # de -1 até -10 pulando -1
# ou 
print(variavel[-1:-10:-1])
