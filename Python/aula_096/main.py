import os
# Criando arquivos com python
# Usamos a função open para abrir 
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita e criação caso não exista), x (para criação)
# a (escreva ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# módulo os:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou movo o arquivo
# módulo json:
# jason.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\laragon\\www\\Python\\aula_096\\'
caminho_arquivo += 'index.txt'

# arquivo = open(caminho_arquivo,  'w')
# Não esqueça de fechar o arquivo com essa abordagem
# arquivo.close()

# Arquivo fechado automaticamente
with open(caminho_arquivo, 'w') as arquivo:
    ...

# o enconding é para o windows abrir o arquivo em utf-8
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Primeira linha\n')
    arquivo.write('Segunda linha\n')
    arquivo.writelines(
        ('Linha 3 \n', 'Linha 4 \n')
        )
    # Voltar ao topo
    arquivo.seek(0,0)
    # Lê todo o arquivo
    # print(arquivo.read())
    arquivo.seek(0,0)

    # Lendo uma linha
    # end é para tirar a quebra de linha que possui
    print(arquivo.readline(), end='')
    print(arquivo.readline())

    print('READLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())
    
    arquivo.write('Atenção \n')

print()
print('#' * 10)
print()

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

# Com 'a' eu não apago o que há no arquivo
# ele adiciona ao final
with open(caminho_arquivo, 'a') as arquivo:
    arquivo.write('Linha 5 \n')

# Remover um arquivo
# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)

# Renomear arquivo
os.rename(caminho_arquivo, 'C:\\laragon\\www\\Python\\aula_096\\novo_nome.txt')


