# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual é o salário do Funcinário? R$ '))
r = s + (s * 0.15)
print(f'Um funcionário que ganhava R${s:.2f}, com 15% de aumento, passa a receber R${r:.2f}.')