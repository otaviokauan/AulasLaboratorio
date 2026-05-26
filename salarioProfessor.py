parada = 0

while parada != 99999:
    sexo = input("Digite M para masculino ou F para Feminino: ")
    hrAula = int(input("Quantas horas aulas você tem por mês? "))
    salarioB = 30 * hrAula

    match sexo:
        case "M":
            salarioL = salarioB - (salarioB * 0.10)
            print(f"Seu salario bruto é R${salarioB:g} e seu salario liquido é R${salarioL:g}")
        
        case "F":
            salarioL = salarioB - (salarioB * 0.05)
            print(f"Seu salario bruto é R${salarioB:g} e seu salario liquido é R${salarioL:g}")
        
        case _: 
            print("Gênero inválido!!!")

    parada = float(input("Digite 99999 para sair ou 0 para continuar: "))

print("Programa encerrado.")