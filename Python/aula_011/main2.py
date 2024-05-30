# Formatação de Strings
# Método format
a = 'A'
b = 'B'
c = 1.2

formato = 'a={} b={} c={:.2f}'.format(a,b,c)
numerado = '{2:.2f} b={0} a={2} b={1}'.format(a,b,c)
nomeado = 'a={nome1} a={nome1} b={nome2} c={nome3:.2f}'.format(
    nome1 = a, nome2=b, nome3=c
)
print(formato)
print(numerado)
print(nomeado)