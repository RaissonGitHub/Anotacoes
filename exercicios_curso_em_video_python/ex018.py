#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'O ângulo de {a:.2f} tem o SENO de {s:.2f}')
print(f'O ângulo de {a:.2f} tem o COSSENO de {c:.2f} ')
print(f'O ângulo de {a:.2f} tem a TANGENTE de {t:.2f}')