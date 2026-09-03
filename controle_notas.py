# Controle de Notas
# Sistema de menu para cadastrar alunos com 3 notas, calcular a media
# ponderada (25/35/40), exibir o boletim, consultar um aluno por nome
# e gerar o ranking dos 3 melhores (ordenacao manual, tipo bubble sort).

alunos = []

opcao = -1

while opcao != 0:

    print("\n=== CONTROLE DE NOTAS ===")
    print("1 - Cadastrar aluno")
    print("2 - Exibir boletim")
    print("3 - Consultar aluno")
    print("4 - Ranking dos 3 melhores")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        nome = input("Nome do aluno: ")

        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        aluno = (
            nome,
            nota1,
            nota2,
            nota3
        )

        alunos.append(aluno)

        print("Aluno cadastrado.")

    elif opcao == 2:

        if len(alunos) == 0:

            print("Nenhum aluno cadastrado.")

        else:

            print("\n=== BOLETIM ===")

            for aluno in alunos:

                media = (
                    aluno[1] * 0.25 +
                    aluno[2] * 0.35 +
                    aluno[3] * 0.40
                )

                if media >= 6:

                    situacao = "APROVADO"

                else:

                    situacao = "REPROVADO"

                print(
                    aluno[0],
                    "| Média:",
                    round(media, 2),
                    "|",
                    situacao
                )

    elif opcao == 3:

        busca = input("Nome do aluno: ")

        encontrado = False

        for aluno in alunos:

            if aluno[0].lower() == busca.lower():

                media = (
                    aluno[1] * 0.25 +
                    aluno[2] * 0.35 +
                    aluno[3] * 0.40
                )

                print("\nNome:", aluno[0])
                print(
                    "Média:",
                    round(media, 2)
                )

                encontrado = True

        if not encontrado:

            print("Aluno não encontrado.")

    elif opcao == 4:

        if len(alunos) == 0:

            print("Nenhum aluno cadastrado.")

        else:

            ranking = []

            for aluno in alunos:

                media = (
                    aluno[1] * 0.25 +
                    aluno[2] * 0.35 +
                    aluno[3] * 0.40
                )

                ranking.append(
                    (
                        aluno[0],
                        media
                    )
                )

            for i in range(len(ranking)):

                for j in range(
                    i + 1,
                    len(ranking)
                ):

                    if (
                        ranking[j][1]
                        >
                        ranking[i][1]
                    ):

                        aux = ranking[i]

                        ranking[i] = ranking[j]

                        ranking[j] = aux

            print("\n=== TOP 3 ===")

            limite = 3

            if len(ranking) < 3:

                limite = len(ranking)

            for i in range(limite):

                print(
                    i + 1,
                    "º lugar:",
                    ranking[i][0],
                    "- Média:",
                    round(
                        ranking[i][1],
                        2
                    )
                )

    elif opcao == 0:

        print("Programa encerrado.")

    else:

        print("Opção inválida.")
