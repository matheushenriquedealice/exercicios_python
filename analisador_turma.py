# Analisador de Turma
# Cadastra alunos e notas, calcula media da turma, maior e menor nota,
# separa aprovados/reprovados e monta um histograma simples das notas.

nomes = []
notas = []

print("\n=== ANALISADOR DE TURMA ===")

while True:

    nome = input(
        "Nome do aluno (fim para encerrar): "
    )

    if nome.lower() == "fim":
        break

    nota = float(input("Nota: "))

    nomes.append(nome)
    notas.append(nota)

if len(notas) == 0:

    print("Nenhum aluno cadastrado.")

else:

    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    maior_nota = notas[0]
    menor_nota = notas[0]

    nome_maior = nomes[0]
    nome_menor = nomes[0]

    for i in range(len(notas)):

        if notas[i] > maior_nota:

            maior_nota = notas[i]
            nome_maior = nomes[i]

        if notas[i] < menor_nota:

            menor_nota = notas[i]
            nome_menor = nomes[i]

    aprovados = []
    reprovados = []

    for i in range(len(notas)):

        if notas[i] >= 6:

            aprovados.append(nomes[i])

        else:

            reprovados.append(nomes[i])

    faixa1 = 0
    faixa2 = 0
    faixa3 = 0
    faixa4 = 0
    faixa5 = 0

    for nota in notas:

        if nota <= 2:
            faixa1 += 1

        elif nota <= 4:
            faixa2 += 1

        elif nota <= 6:
            faixa3 += 1

        elif nota <= 8:
            faixa4 += 1

        else:
            faixa5 += 1

    print("\n=== RELATÓRIO ===")

    print(
        "Média da turma:",
        round(media, 2)
    )

    print(
        "Maior nota:",
        nome_maior,
        "-",
        maior_nota
    )

    print(
        "Menor nota:",
        nome_menor,
        "-",
        menor_nota
    )

    print("\nAprovados:", aprovados)
    print("Reprovados:", reprovados)

    print("\n--- HISTOGRAMA ---")
    print("0-2 :", "#" * faixa1)
    print("3-4 :", "#" * faixa2)
    print("5-6 :", "#" * faixa3)
    print("7-8 :", "#" * faixa4)
    print("9-10:", "#" * faixa5)
