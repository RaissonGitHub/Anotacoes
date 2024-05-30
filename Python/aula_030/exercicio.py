# Calculadora com while

while True:
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")

    if n1.isdigit() and n2.isdigit():
        op_permidos = "+-*/"
        op = input("Digite uma operação: [ + - * / ]: ")
        if op not in op_permidos:
            print("Operador inválido")
            continue
        if len(op) > 1 :
            print('Digite apenas um operador')
            continue
        else:
            int_n1 = int(n1)
            int_n2 = int(n2)

            if op == "+":
                print(int_n1 + int_n2)
            elif op == "-":
                print(int_n1 - int_n2)
            elif op == "*":
                print(int_n1 * int_n2)
            elif op == "/":
                print(int_n1 / int_n2)

            # sair
            sair = input("Quer sair? [s]im: ").lower().startswith("s")
            if sair is True:
                break
    else:
        print("Numeros não válidos")
        continue
