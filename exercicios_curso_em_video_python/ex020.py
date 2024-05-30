# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = input('Primeiro nome:')
n2 = input('Segundo nome:')
n3 = input('Terceiro nome:')
n4 = input('Quarto nome:')
nomes = [n1,n2,n3,n4]
random.shuffle(nomes)
print('A ordem de apresentação será')
print(nomes)