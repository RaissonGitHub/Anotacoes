"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

v = int(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${(v-80)*7:.2f}!')