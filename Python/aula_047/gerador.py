import random

nove_digitos =  ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))
contador = 10
soma = 0
for i, numero in enumerate(nove_digitos):
    numero_multiplicado = int(numero) * contador
    soma += numero_multiplicado
    contador -= 1
produto = soma * 10
resto_divisao = produto % 11
p_digito = 0 if resto_divisao > 9 else resto_divisao


# Segundo digito inclui todos os passos anteriores mas incluindo o penultimo digito
dez_digitos = nove_digitos[:9] + f'{p_digito}'
contador = 11
soma = 0
for i, numero in enumerate(dez_digitos):
    numero_multiplicado = int(numero) * contador
    soma += numero_multiplicado
    contador -= 1
produto = soma * 10
resto_divisao = produto % 11
u_digito = 0 if resto_divisao > 9 else resto_divisao

cpf_gerado_pelo_calculo = f'{nove_digitos}{p_digito}{u_digito}'
print(cpf_gerado_pelo_calculo)


