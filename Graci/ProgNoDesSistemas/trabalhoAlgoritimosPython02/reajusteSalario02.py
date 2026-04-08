salario = float(input("Digite o salário do funcionário: "))
salario2 = salario * 0.93

if salario <= 350:
    reajuste2 = salario2 + 100
    print(f"O seu salário após o Lula é: {reajuste2:g}")
elif salario > 350 and salario <= 600:
    reajuste2 = salario2 + 75
    print(f"O seu salário após o Lula é: {reajuste2:g}")
elif salario > 600 and salario <= 900:
    reajuste2 = salario2 + 50
    print(f"O seu salário após o Lula é: {reajuste2:g}")
else: 
    reajuste = salario2
    print (f"O seu salário após o Lula é: {reajuste:g}")

    #OTAVIO 