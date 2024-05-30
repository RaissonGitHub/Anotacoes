# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma varável e mostre o valor
# da variável.

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplicar(*args):
    total = 1
    for i in args:
        total *= i
    return total
    

multi = multiplicar(2,3,4)
print(multi)

def par_impar(n):
    if n % 2 == 0:
        return 'par'
    return 'ímpar'

print(par_impar(2))