# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
m2 = l*a
print(f'Sua parede tem a dimensão de {l:.2f}x{a:.2f} e sua área é de {m2}m².')
print(f'Para pintar essa parede, você precisará de {m2/2}l de tinta.')