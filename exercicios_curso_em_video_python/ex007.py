# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = int(input('Digite a 1 nota: '))
n2 = int(input('Digite a 2 nota: '))
m = (n1+n2) / 2
print(f'A média entre {n1:.1f} e {n2:.1f} é igual a {m:.1f}')