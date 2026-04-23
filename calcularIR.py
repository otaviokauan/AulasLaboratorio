salarioc = float(input("qual o seu salario da contribuição? "))
desconto = float(input("qual o seu desconto da previdencia? "))
quantidaDependente = float(input("qual a quantidade de dependentes? "))
deducaoDependente = 164.56

salarioBaseIR  = salarioc - desconto - deducaoDependente * quantidaDependente


if salarioBaseIR <= 1637.11:
    print(f"o valor do seu salario é {salarioBaseIR:g}")
elif salarioBaseIR > 1637.11 and salarioBaseIR <= 2452.50:
    salarioBaseIR = salarioBaseIR * 0.075
    print(f"o valor do seu salario é {salarioBaseIR:g}")
elif salarioBaseIR > 2452.50 and salarioBaseIR <= 3271.38:
    salarioBaseIR = salarioBaseIR * 0.15
    print(f"o valor do seu salario é {salarioBaseIR:g}")
elif salarioBaseIR > 3271.38 and salarioBaseIR <= 4087.65:
 salarioBaseIR = salarioBaseIR * 0.225
 print(f"o valor do seu salario é {salarioBaseIR:g}")
else:
 salarioBaseIR = salarioBaseIR * 0.275
 print(f"o valor do desconto é {salarioBaseIR:g}")