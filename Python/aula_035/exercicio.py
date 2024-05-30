"""
Faça um jogo para o usuário adivinhar qual 
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para o
usuário digitar apenas uma letra.
- Quando o usário digitar uma letra, você
vai conferir se a letra digitada está 
na pavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver 
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu 
usuário.
"""

contador = 0
secreta = 'azul'
formar = ''
while True : 
    inp = input('Digite uma letra: ')
    if len(inp) > 1 :
        print('Digite apenas uma letra')
    else:
        if inp in secreta :
            formar += inp
        f = ''
        for letra in secreta :
            if letra in formar :
                f+=(letra)
            else:
                f+=("*")
        print(f)
        
    contador +=1
    if formar == secreta :
        print('Você ganhou')
        print(f'Tentativas: {contador}')
        break
    