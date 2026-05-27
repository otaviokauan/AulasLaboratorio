valor = float(input("Digite o valor do produto: "))

if valor <= 50:
    reajuste = valor * 1.05
elif valor > 50 and valor <= 100:
    reajuste = valor * 1.10
else:
    reajuste = valor * 1.15
print(f"Valor reajustado: R$ {reajuste:.2f}")

#Otavio