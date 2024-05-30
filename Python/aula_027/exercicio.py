"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro.
"""

n = input("Digite um número inteiro: ")
if n.isdigit():
    n_int = int(n)
    if n_int % 2 == 0:
        print(f"{n_int} é par")
    else:
        print(f"{n_int} é ímpar")

else:
    print("Não é um número inteiro")

print("-" * 100)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite a hora atual: ")
try:
    h_int = int(hora)
    if h_int >= 0 and h_int <= 11:
        print("Bom dia")
    elif h_int > 11 and h_int <= 17:
        print("Boa tarde")
    elif h_int > 17 and h_int < 24:
        print("Boa noite")
except:
    print('Não conheço essa hora')

print("-" * 100)


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva
'Seu nome é normal'; maior que 6 escreva 'Seu nome é muito grande'.
"""

nome = input("Digite seu nome: ")
tam = len(nome)
if tam < 4:
    print("Seu nome é muito curto")
elif tam > 4 and tam < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
