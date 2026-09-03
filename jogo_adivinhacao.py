# Jogo de Adivinhação
# Sorteia um numero de 1 a 100, da ate 7 tentativas por rodada e pontua
# conforme o numero de tentativas usadas. Guarda o historico de rodadas
# e permite jogar varias rodadas seguidas, somando a pontuacao total.

import random

historico = []

pontuacao_total = 0
rodada = 1

jogar = "s"

while jogar.lower() == "s":

    numero_secreto = random.randint(
        1,
        100
    )

    tentativas = 0
    acertou = False

    print(
        "\n=== RODADA",
        rodada,
        "==="
    )

    while tentativas < 7:

        chute = int(
            input("Digite seu chute: ")
        )

        tentativas += 1

        if chute == numero_secreto:

            acertou = True

            if tentativas == 1:
                pontos = 100

            elif tentativas == 2:
                pontos = 85

            elif tentativas == 3:
                pontos = 70

            elif tentativas == 4:
                pontos = 55

            elif tentativas == 5:
                pontos = 40

            elif tentativas == 6:
                pontos = 25

            else:
                pontos = 10

            print(
                "Você acertou em",
                tentativas,
                "tentativas!"
            )

            print(
                "Pontuação:",
                pontos
            )

            break

        elif chute < numero_secreto:

            print(
                "O número é maior."
            )

        else:

            print(
                "O número é menor."
            )

    if not acertou:

        pontos = 0

        print(
            "Você perdeu!"
        )

        print(
            "O número era:",
            numero_secreto
        )

    pontuacao_total += pontos

    historico.append(
        (
            rodada,
            numero_secreto,
            tentativas,
            pontos
        )
    )

    jogar = input(
        "\nJogar novamente? (s/n): "
    )

    rodada += 1

print("\n=== HISTÓRICO ===")

for item in historico:

    print(
        "Rodada:",
        item[0],
        "| Número:",
        item[1],
        "| Tentativas:",
        item[2],
        "| Pontos:",
        item[3]
    )

print(
    "\nPONTUAÇÃO TOTAL:",
    pontuacao_total
)
