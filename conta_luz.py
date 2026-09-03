# Cálculo de Conta de Luz
# Calcula o valor da conta de energia a partir do consumo em kWh e do
# tipo de instalação (residencial, comercial ou industrial), cada uma
# com sua propria tarifa e faixa de consumo.

quantidade_kWh = int(input('informe quantos kWh foram consumidos por mes?'))
tipo_instalação = input('Informe o tipo de instalação: R para residencia , I para industria e C para comercio: ')

if tipo_instalação == 'R':
    if quantidade_kWh <= 500:
        preco = quantidade_kWh * 0.40
        print(f'O valor a pagar é de R$ {preco:.2f} reais')
    else:
        preco = quantidade_kWh * 0.65
        print(f'O valor a pagar é de R$ {preco:.2f} reais')

if tipo_instalação == 'C':
    if quantidade_kWh <= 1000:
        preco = quantidade_kWh * 0.55
        print(f'O valor a pagar é de R$ {preco:.2f} reais')
    else:
        preco = quantidade_kWh * 0.60
        print(f'O valor a pagar é de R$ {preco:.2f} reais')

if tipo_instalação == 'I':
    if quantidade_kWh <= 5000:
        preco = quantidade_kWh * 0.55
        print(f'O valor a pagar é de R$ {preco:.2f} reais')
    else:
        preco = quantidade_kWh * 0.60
        print(f'O valor a pagar é de R$ {preco:.2f} reais')
