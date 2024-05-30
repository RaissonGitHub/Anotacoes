# Introdução as Generator Functions em Python
# generator = (n for n in range(10000000))

def generator(n=0):
    yield 1 # Pausar
    print('continuando...')
    yield 2 # Pausar

ge = generator(n=0)
print(next(ge))
print(next(ge))
