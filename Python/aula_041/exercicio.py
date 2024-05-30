# Lista de compras
# Inserir, apagar, listar
import os

lista = []

while True:
    print("Selecione uma opção")
    acao = input("[i]nserir, [a]pagar, [l]istar: ")
    acao = acao.lower()
    if acao == "i":
        os.system('cls') # limpar o terminal
        compra = input("Valor: ")
        lista.append(compra)
    elif acao == "a":
        apagar = input("Escolha o índice para apagar: ")
        if apagar.isdigit():
            apagar_int = int(apagar)
            if len(lista) > apagar_int:
                del lista[apagar_int]
            else:
                print("Não foi possível apagar este índice")
    elif acao == "l":
        if len(lista) > 0 :
            for indice, item in enumerate(lista):
                print(f"{indice}  {item}")
        else:
            print('Nada para listar')
    else:
        print("Opção inválida")
