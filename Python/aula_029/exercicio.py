# Iterando strings com while

nome = 'Rafael Pereira'

tam = len(nome)

i = 0
s = ''
while i < tam :
    s += f'*{nome[i]}'
    i+=1
s+='*'
print(s)