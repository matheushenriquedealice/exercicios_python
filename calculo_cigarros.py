# Cálculo de Cigarros
# A partir de quantos cigarros por dia e ha quantos anos a pessoa fuma,
# estima quantos cigarros ja foram fumados e quantos dias de vida
# equivalentes foram perdidos (considerando 10 min perdidos por cigarro).

cigarro_dia = int(input('quantos cigarros voce fuma por dia? '))
anos_fumo = int(input('quantos anos voce fuma? '))

cigarros_fumados = cigarro_dia * (anos_fumo * 365)
dia_perdido = int((cigarros_fumados * 10) / 1440)
print(f'voce fumou {cigarros_fumados} cigarros em {anos_fumo} anos, e você perdeu {dia_perdido} dias de vida')
