# Laço for in

texto = 'Python'
n_str = ''
for letra in texto:
    n_str += f'*{letra}'
    print(letra)
n_str +='*'
print(n_str)

# for + range
# range ->(start,stop,step)
# for e range são independentes

n1 = range(10) # começa do 0 até 10
n2 = range(5,10) # começa do 5 até 10
n3 = range(5,10,2) # começa do 5 até 10 pulando 2
print(n1)
print(n2)
print(n3)

numeros = range(10)

for numero in n1 :
    print(numero)