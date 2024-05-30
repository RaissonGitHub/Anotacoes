# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

n = input('Qual o seu nome completo? ').lower()
print(f'Seu nome tem Silva? {'Silva' in n}')