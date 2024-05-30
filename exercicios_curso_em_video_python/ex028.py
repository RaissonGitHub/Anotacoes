"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
import time
r = random.randint(0,5)
v = int(input('Em que número eu pensei? '))
print('Processando...')
time.sleep(3)
if r == v :
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {r} e não no {v}!')