valor = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(valor)}')
print(f'Só tem espaços? {valor.isspace()}')
print(f'É numérico? {valor.isnumeric()}')
print(f'É alfabetico? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está capitalizada? {valor.istitle()}')