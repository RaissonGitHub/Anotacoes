"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Corvension flags - !r !s !a
"""

variavel = "abc"
print(f"{variavel}")

print(f"{variavel: >10}")  # coloca espaços na esquerda até conter 10 caracteres
print(f"{variavel:0>10}")

print(f"{variavel: <10}.")  # coloca espaços na direita até conter 10 caracteres
print(f"{variavel:-<10}.")

print(f"{variavel:_^10}")  # coloca espaços envolta
print(f"{variavel: ^10}")

print(f'{-1000.73409742:,.1f}') # o separador de milhar agora é uma ,
print(f'{1000.73409742:+.1f}') # mostra o sinal + quando positivo
print(f'{1000.73409742:0=+10.1f}') # mostra o sinal + quando positivo e preenche até 10 caracteres
print(f'o Hexadecimal de 1500 é {1500:08X}')