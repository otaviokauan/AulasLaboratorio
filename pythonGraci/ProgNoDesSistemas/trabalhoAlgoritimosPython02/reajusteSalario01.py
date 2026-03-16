salario = float(input("Digite o salário do funcionário: "))
if salario <= 300:
    reajuste = salario * 1.15
    print(f"O seu salário reajustado é: {reajuste:g}")
elif salario > 300 and salario <= 600:
    reajuste = salario * 1.10 
    print(f"O seu salário reajustado é: {reajuste:g}")
elif salario > 600 and salario <= 900:
    reajuste = salario * 1.05
    print(f"O seu salário reajustado é: {reajuste:g}")
else:   
    print("O seu salário não está dentro das normas, ele não receberá reajuste.")

    #OTAVIO