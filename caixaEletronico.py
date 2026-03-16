valor = float(input("Digite o valor que deseja sacar (Máx R$600 e min R$10): "))

if valor < 10 or valor > 600:
    print("Valor inválido. O valor deve ser entre R$10 e R$600.")
else:
    notas100 = valor // 100
    valor = valor % 100

    notas50 = valor // 50
    valor = valor % 50

    notas20 = valor // 20
    valor = valor % 20

    notas10 = valor // 10
    valor = valor % 10
    
    notas5 = valor // 5
    valor = valor % 5

    notas2 = valor // 2 
    valor = valor % 2

    notas1 = valor // 1
    valor = valor % 1

    print(f"Notas de R$100: {notas100:g}")
    print(f"Notas de R$50: {notas50:g}")
    print(f"Notas de R$20: {notas20:g}")
    print(f"Notas de R$10: {notas10:g}")
    print(f"Notas de R$5: {notas5:g}")
    print(f"Notas de R$2: {notas2:g}")
    print(f"Notas de R$1: {notas1:g}")
    