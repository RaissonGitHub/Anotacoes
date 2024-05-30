# Formatação de strings
# f-strings

nome = "Luiz Reginaldo"
altura = 1.80
peso = 77
imc = peso / (altura * altura)
# f de format | :.2f duas casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Reginaldo tem 1.8 de altura,
# pesa 77 quilos e seu IMC é
# 23.76543209876543
