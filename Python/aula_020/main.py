"""
Interpolação básica de strings
s- string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavavel_1 = 'O nome informado é %s' % nome
variavavel_2 = '%s fez uma compra de R$%.2f reais' % (nome,preco)
variavavel_3 = 'Mais especificamente R$%f reais' % preco
print(variavavel_1)
print(variavavel_2)
print(variavavel_3)
print('O hexadecimal de %d é %x ou' % (15,15))
print('O hexadecimal de %d é %04x ou' % (15,15))
print('O hexadecimal de %d é %04X ou' % (15,15))
print('O hexadecimal de %d é %08X ' % (15,15))