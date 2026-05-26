senhaCorreta = "1234"
senhaEntrada = input("Digite a senha: ")

if senhaEntrada == senhaCorreta:
    votosA = 0
    votosB = 0
    votosC = 0
    votosBranco = 0
    votosNulo = 0
    totalVotantes = 0
    voto = ""

    while voto != "$":
        voto = input("Voto: ")
        
        if voto == "$":
            break
            
        totalVotantes = totalVotantes + 1
        
        match voto:
            case "a":
                votosA = votosA + 1
            case "b":
                votosB = votosB + 1
            case "c":
                votosC = votosC + 1
            case "0":
                votosBranco = votosBranco + 1
            case _:
                votosNulo = votosNulo + 1

    votosExpressos = votosA + votosB + votosC
    percA = percB = percC = 0

    if votosExpressos > 0:
        percA = (votosA / votosExpressos) * 100
        percB = (votosB / votosExpressos) * 100
        percC = (votosC / votosExpressos) * 100

    print(f"\nTotal de votantes: {totalVotantes}")
    print(f"Votos nulos: {votosNulo}")
    print(f"Votos brancos: {votosBranco}")
    print(f"Candidato A: {votosA} ({percA:.1f}%)")
    print(f"Candidato B: {votosB} ({percB:.1f}%)")
    print(f"Candidato C: {votosC} ({percC:.1f}%)")

    maiorVotacao = 0
    if votosA > maiorVotacao: maiorVotacao = votosA
    if votosB > maiorVotacao: maiorVotacao = votosB
    if votosC > maiorVotacao: maiorVotacao = votosC

    if maiorVotacao > 0:
        textoVencedores = ""
        if votosA == maiorVotacao: textoVencedores = textoVencedores + "A "
        if votosB == maiorVotacao: textoVencedores = textoVencedores + "B "
        if votosC == maiorVotacao: textoVencedores = textoVencedores + "C "
        
        print(f"Vencedor(es): {textoVencedores}")

        if maiorVotacao > (totalVotantes / 2):
            print("MAIORIA ABSOLUTA")
        else:
            print("Não houve maioria absoluta")
    else:
        print("Nenhum voto computado para candidatos")

else:
    print("Senha Incorreta")