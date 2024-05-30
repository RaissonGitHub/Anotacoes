# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

n1 = input('Primeiro nome:')
n2 = input('Segundo nome:')
n3 = input('Terceiro nome:')
n4 = input('Quarto nome:')
nomes = [n1,n2,n3,n4]
e = random.choice(nomes)
print(f'O aluno escolhido foi {e}')