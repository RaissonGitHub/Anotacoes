# dir, hasattr, getattr em Python

string = 'Ricardo'
metodo = 'upper'
# todos os métodos definidos dentro da string
print(dir(string))


# checar se a string possui um método
if hasattr(string, 'lower'):
    print('Possui lower')
    print(string.lower())

# executar um método
print(getattr(string,metodo)())