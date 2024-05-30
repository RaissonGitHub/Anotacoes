"""
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome completo: ')
nome_separado = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras')