# Desempacotamento em chamadas
# de métodos e funções 
string = 'ABCD'
lista = ["Maria", "Helena",1,2,3,'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista # u = ultimo | ap = penultimo
# print(p, u, ap)

print("Maria", "Helena",1,2,3,'Eduarda') # mesmo que
# todos os valores para o print
print(*lista)
print(*string)
print(*tupla)