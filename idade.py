ano = float(input("digite sua idade em anos (idade em anos) "))
meses = float(input("digite sua idade em meses (ex: 15 anos e 5 meses, eu quero saber a quantidade de meses) "))
dias = float (input("digite sua idade em dias (ex: 15 anos 5 meses e 10 dias, quero saber os dias) "))

resultado1 = ano * 365
resultado2 = meses * 30
resultado3 = resultado1 + resultado2 + dias

print(f"você viveu por {resultado3:g}")