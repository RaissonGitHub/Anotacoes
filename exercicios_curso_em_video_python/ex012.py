# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual é o preço do produto? R$ '))
d = p - (p * 0.05)
print(f'O produto que custava R${p:.2f} na promoção de 5% vai custar R${d:.2f}')