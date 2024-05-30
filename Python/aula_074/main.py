# Yield from 

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g  = gen2()
for n in g:
    print(n)