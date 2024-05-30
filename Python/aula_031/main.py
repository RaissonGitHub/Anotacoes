# while/else
# O else é executado ao fim do while
# Mas se houver algum break no loop
# O else não será executado

string = 'Valor'

i = 0
while i < len(string) :
    letra = string[i]
    if letra == ' ' :
        break
    print(letra)
    i+=1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
