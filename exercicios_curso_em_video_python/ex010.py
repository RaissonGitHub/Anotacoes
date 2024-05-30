# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

d = float(input('Quanto dinheiro você tem na carteira? R$ '))

print(f'Com {d:.2f} você pode comprar US${d/4.98:.2f}')