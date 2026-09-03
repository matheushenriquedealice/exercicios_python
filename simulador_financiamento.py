# Simulador de Financiamento Imobiliário
# Verifica se um financiamento pode ser aprovado: a prestação mensal
# (valor da casa dividido pelo numero de meses) nao pode ultrapassar
# 30% do salario do interessado.

valor_casa = float(input('Qual o valor da casa que deseja comprar?'))
salario = float(input('Qual seu salario? '))
quantidade_anos = int(input('Quantos anos voce pretende pagar?'))

valor_prestação = valor_casa / (quantidade_anos * 12)

salario2 = salario * 0.30

if salario2 >= valor_prestação:
    print('Emprestimo foi aprovado')
else:
    print('Emprestimo não foi aprovado')
