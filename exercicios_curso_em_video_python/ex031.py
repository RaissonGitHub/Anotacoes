"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

d = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d:.1f}Km.')
if d < 200:
    p = d * 0.5
else:
    p = d * 0.45
print(f'E o preço da sua passagem será de R${p:.2f}')
