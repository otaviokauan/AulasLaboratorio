salario = float (input("Seu salario é qual? "));
porcentagem = float (input("Qual a porcentagem de reajuste? "));

reajusteSalario = (porcentagem/100) + 1
reajuste = salario * 1.25

print(f"Seu novo salario é {reajuste:g}")