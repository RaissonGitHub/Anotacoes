# Exercicio - sistema de perguntas e respostas

perguntas = [
    {
        "Pergunta": "Quanto é 2+2",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]
qt_acertos = 0
for pergunta in perguntas:
    print(pergunta["Pergunta"])

    for i, opcao in enumerate(pergunta["Opções"]):
        print(f"{i}) {opcao}")

    escolha = input("Escolha uma opção: ")
    escolha_int = None
    acertou = False

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < len(pergunta["Opções"]):
            r_final = pergunta["Opções"][escolha_int]

            if r_final == pergunta["Resposta"]:
                acertou = True
            else:
                acertou = False
        if acertou:
            print("Acertou")
            qt_acertos += 1
        else:
            print("Errou")

print(f"{qt_acertos} acertos de {len(perguntas)} perguntas")
