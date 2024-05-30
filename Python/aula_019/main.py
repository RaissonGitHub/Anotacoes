# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 
#  R a f a e l
# -6-5-4-3-2-1
nome = 'Rafael'
print(nome[2])
print(nome[-4])

print('l' in nome)
print('x' in nome)
print('ae' in nome)
print('Ra' not in nome)

nome = input('Digite um nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome :
    print(f'{encontrar} está em {nome}')
else:
    
    print(f'{encontrar} não está em {nome}')