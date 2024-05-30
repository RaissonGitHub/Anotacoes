# Contornando impressisões com pontos flutuantes
import decimal

n1 = 0.1
n2 = 0.7
n3 = n1 + n2
print(n3)
print(f'{n3:.2f}') # string
print(round(n3,2)) # float


print('-'*50)

# Para uma conta extremamente precisa com inúmeras casas decimais

n1 = decimal.Decimal('0.1') # o número informado deve ser em string
n2 = decimal.Decimal('0.7')
n3 = n1 +n2

print(n3)
print(f'{n3:.2f}') # string
print(round(n3,2)) # float