from datetime import date
"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

birth_year = int(input('Digite o ano de nascimento: '))
age = date.today().year - birth_year

category = 'MIRIM' if age <= 9 else 'INFANTIL' if age <= 14 else 'JÚNIOR' if age <= 19 else 'SÊNIOR' if age <= 25 else 'MASTER'

print(category)