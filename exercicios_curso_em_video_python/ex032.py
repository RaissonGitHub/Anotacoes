#  Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não é bissexto")

