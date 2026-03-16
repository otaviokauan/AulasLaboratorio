print("## Programa de Empréstimo ##. Responda: (0 - Não e 1 - Sim)")
nomeNegativo = int(input("Possui nome negativo? "))
if nomeNegativo == 1:
    print("Empréstimo negado.")
else:
    carteriraTrabalho = int(input("Possui carteira de trabalho? "))
    if carteriraTrabalho == 0:
        print("Empréstimo negado.")
    else:
        possuiCasaProria = int(input("Possui casa própria? "))
    if possuiCasaProria == 0:
            print("Empréstimo negado.")
    else:
         print("Empréstimo aprovado.")
