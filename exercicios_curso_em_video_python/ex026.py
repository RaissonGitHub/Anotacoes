# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

f = input('Digite uma frase: ').lower().strip()
print(f'A letra A aparece {f.count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {f.find("a")}')
print(f'A última letra A apareceu na posição {f.rfind("a")}')
