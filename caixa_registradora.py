# Caixa Registradora
# Cadastra produtos e precos, calcula o subtotal, aplica um desconto
# progressivo conforme o valor da compra e imprime o cupom fiscal.

produtos = []
precos = []

subtotal = 0

print("\n=== CAIXA REGISTRADORA ===")

while True:

    produto = input("Produto (fim para encerrar): ")

    if produto.lower() == "fim":
        break

    preco = float(input("Preço: "))

    produtos.append(produto)
    precos.append(preco)

    subtotal += preco

if len(produtos) == 0:

    print("Nenhum produto cadastrado.")

else:

    if subtotal < 50:
        percentual = 0

    elif subtotal < 100:
        percentual = 5

    else:
        percentual = 10

    desconto = subtotal * (percentual / 100)
    total = subtotal - desconto

    print("\n=== CUPOM FISCAL ===")

    for i in range(len(produtos)):

        print(
            produtos[i],
            "........ R$",
            format(precos[i], ".2f")
        )

    print("----------------------")
    print("Subtotal: R$", format(subtotal, ".2f"))
    print(
        "Desconto:",
        percentual,
        "% = R$",
        format(desconto, ".2f")
    )
    print("TOTAL: R$", format(total, ".2f"))
