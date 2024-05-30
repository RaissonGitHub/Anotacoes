"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomemeado recebe apenas o argumento (valor)
"""


def soma(x, y):
    # Definição
    print(f"{x=}  {y=}", "|", "x + y = ", x + y)


soma(1, 2)
soma(y=2, x=1)

# Nao recomendado
soma(2, x=1)
# soma(x=1,2) # Erro! Após colocar um argumento nomeado os próximos também devem ser nomeados
