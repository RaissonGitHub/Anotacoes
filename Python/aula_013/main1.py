# if / elif / else

entrada = input('Você quer "entrar" ou "sair"')

# Hierarquia da identação
if entrada == 'entrar' : 
    print('Você entrou no sistema')
elif entrada == 'sair' : 
    print('Você saiu do sistema')
else: 
    print('Você não digitou nem entra ou sair')
print('Fora dos blocos')