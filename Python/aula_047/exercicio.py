"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regresiva começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9   8   7   6   5   4   3   2
*   7   4   6   8   2   4   8   9   0
    70  36  48  56  12  20  32  27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
import sys

cpf_enviado_usuario = "93447736453" \
     .replace('.','') \
     .replace('-','')
# retirar . e - substituir por nada
cpf_sequencial = cpf_enviado_usuario ==cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
if cpf_sequencial:
    sys.exit() # fechar o programa
nove_digitos = cpf_enviado_usuario[:9]
contador = 10
soma = 0
for i, numero in enumerate(nove_digitos):
    numero_multiplicado = int(numero) * contador
    soma += numero_multiplicado
    contador -= 1
produto = soma * 10
resto_divisao = produto % 11
p_digito = 0 if resto_divisao > 9 else resto_divisao
print(p_digito)


# Segundo digito inclui todos os passos anteriores mas incluindo o penultimo digito
dez_digitos = cpf_enviado_usuario[:9] + f'{p_digito}'
contador = 11
soma = 0
for i, numero in enumerate(dez_digitos):
    numero_multiplicado = int(numero) * contador
    soma += numero_multiplicado
    contador -= 1
produto = soma * 10
resto_divisao = produto % 11
u_digito = 0 if resto_divisao > 9 else resto_divisao
print(u_digito)

cpf_gerado_pelo_calculo = f'{nove_digitos}{p_digito}{u_digito}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo :
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')