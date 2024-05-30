# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = input('Digite seu nome completo: ').split()
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')