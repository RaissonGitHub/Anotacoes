"""
Repetições
while (enquanto)
"""

contador = 0
while contador < 10:
    print(contador)
    contador += 1
print("Acabou")

# Parando o laço
print('Novo contador, vai para no 4')
contador = 0
while contador < 10:
    print(contador)
    contador += 1
    if contador == 4 :
        break
print("Acabou")

# Pulando uma execução
print('Novo contador, vai pular o 4')
contador = 0
while contador < 10:
    contador += 1
    if contador == 4 :
        print("Pulei")
        continue
    print(contador)
print("Acabou")

print('Novo contador, vai pular o 6 e do 10 até 27 e parar no 43')
contador = 0
while contador <= 50:
    contador+=1
    if contador == 6 :
        print(f'Não vou mostrar o {contador}')
        continue
    if contador >9 and contador < 28:
        print(f'Não vou mostrar o {contador}')
        continue
    if contador == 43 :
        break
    print(f'Meu número é {contador}')
print("Acabou")
