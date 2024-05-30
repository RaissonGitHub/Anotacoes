# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

v = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] conveter para BINÁRIO')
print('[ 2 ] conveter para OCTAL')
print('[ 3 ] conveter para HEXADECIMAL')
o = input('Sua opção: ')
if o == '1':
    print(f'{v} convertido para BINÁRIO é igual a {bin(v)[2:]}')
if o == '2':
    print(f'{v} convertido para OCTAL é igual a {oct(v)[2:]}')
if o == '3':
    print(f'{v} convertido para HEXADECIMAL é igual a {hex(v)[2:]}')