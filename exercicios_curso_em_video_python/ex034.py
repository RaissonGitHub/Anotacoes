#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

si = float(input('Qual é o salário do funcinário? R$ '))

if si > 1250:
    sf = si + (si*0.1)
else:
    sf = si + (si*0.15)
print(f'Quem ganhava R$ {si:.2f} passa a ganhar R$ {sf:.2f} agora')