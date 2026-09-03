# Classificador de IMC
# Le pacientes (nome, peso, altura), calcula o IMC de cada um,
# classifica (abaixo do peso / peso normal / sobrepeso / obesidade)
# e no final mostra um relatorio com o resumo por categoria.

nomes = []
imcs = []
classificacoes = []

abaixo_peso = 0
peso_normal = 0
sobrepeso = 0
obesidade = 0

print("=== CLASSIFICADOR DE IMC ===")

while True:

    nome = input("Nome do paciente: ")

    peso = float(input("Peso (0 para encerrar): "))

    if peso == 0:
        break

    altura = float(input("Altura: "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        abaixo_peso += 1

    elif imc < 25:
        classificacao = "Peso normal"
        peso_normal += 1

    elif imc < 30:
        classificacao = "Sobrepeso"
        sobrepeso += 1

    else:
        classificacao = "Obesidade"
        obesidade += 1

    nomes.append(nome)
    imcs.append(round(imc, 2))
    classificacoes.append(classificacao)

if len(nomes) == 0:

    print("Nenhum paciente cadastrado.")

else:

    print("\n=== RELATÓRIO ===")

    for i in range(len(nomes)):

        print(
            nomes[i],
            "| IMC:",
            imcs[i],
            "|",
            classificacoes[i]
        )

    print("\n--- RESUMO ---")
    print("Abaixo do peso:", abaixo_peso)
    print("Peso normal:", peso_normal)
    print("Sobrepeso:", sobrepeso)
    print("Obesidade:", obesidade)
