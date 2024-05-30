# Exemplo do uso de sets
letras = set()

while True:
    letra = input("digite: ")
    letras.add(letra.lower())

    if "l" in letras:
        print("PARABENS")
        break
    print(letras)
