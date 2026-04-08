num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite a operação (1 para média, 2 para diferença, 3 para multiplicação): "))

if operacao == 1:
    resultado1 = (num1 + num2) / 2
    print("A média é:", resultado1)
elif operacao == 2:
    resultado2 = abs(num1 - num2)
    print("A diferença é:", resultado2)
elif operacao == 3: 
    resultado3 = num1 * num2
    print("A multiplicação é:", resultado3)
else:    
    print("Operação inválida. Por favor, escolha uma operação válida (1, 2 ou 3).")

    #OTAVIO
