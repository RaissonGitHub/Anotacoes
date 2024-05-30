# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

v = float(input("Valor da casa: R$ "))
s = float(input("Salário do comprador: R$ "))
a = int(input("Quantos anos de financiamento? "))

p = v / (12 * a)
if p > v * 0.3:
    print('Empréstimo NEGADO!')
else:
    print(f'Para pagar uma casa de R$ {v:.2f} em {a} anos a prestação será de R$ {p:.2f}')