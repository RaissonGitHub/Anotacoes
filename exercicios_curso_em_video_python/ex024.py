# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

c = input('Em que cidade você nasceu? ').lower()
print(c[:5] == 'santo')