# Tabuada e Treino
# Menu simples: mostra a tabuada de um numero, ou gera 10 perguntas
# aleatorias de multiplicacao para o usuario treinar e ve o aproveitamento.

import random

opcao = 0

while opcao != 3:

    print("\n=== MENU ===")
    print("1 - Ver Tabuada")
    print("2 - Treinar")
    print("3 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:

        numero = int(input("Número: "))

        print("\nTabuada do", numero)

        for i in range(1, 11):

            print(
                numero,
                "x",
                i,
                "=",
                numero * i
            )

    elif opcao == 2:

        acertos = 0

        for i in range(10):

            numero1 = random.randint(1, 10)
            numero2 = random.randint(1, 10)

            resposta = int(
                input(
                    str(numero1)
                    + " x "
                    + str(numero2)
                    + " = "
                )
            )

            correto = numero1 * numero2

            if resposta == correto:

                print("Acertou!")
                acertos += 1

            else:

                print("Errou!")
                print(
                    "Resposta correta:",
                    correto
                )

        percentual = (acertos / 10) * 100

        print("\nAcertos:", acertos)
        print(
            "Aproveitamento:",
            percentual,
            "%"
        )

    elif opcao == 3:

        print("Programa encerrado.")

    else:

        print("Opção inválida.")
