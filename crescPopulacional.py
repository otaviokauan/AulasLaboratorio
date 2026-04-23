PopulacaoA = 80000
PopulacaoB = 200000
ano = 0

while PopulacaoA < PopulacaoB:
    PopulacaoB = PopulacaoB * 1.015
    PopulacaoA = PopulacaoA * 1.03
    ano = ano + 1
    print(f"A população da cidade A esta em {PopulacaoA:g}")
    print(f"A população da cidade B esta em {PopulacaoB:g}")

print(f"A cidade A demorou {ano} anos para alcançar a população de cidade B")