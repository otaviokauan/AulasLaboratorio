salarioAtual = float(input("Digite o salário atual: "))
tempoServico = int(input("Digite o tempo de serviço (em anos): "))

reajuste = 0
bonus = 0

if salarioAtual <= 500:
    reajuste = salarioAtual * 0.25
elif salarioAtual <= 1000:
    reajuste = salarioAtual * 0.20
elif salarioAtual <= 1500:
    reajuste = salarioAtual * 0.15
elif salarioAtual <= 2000:
    reajuste = salarioAtual * 0.10
else:
    reajuste = 0

if tempoServico < 1:
    bonus = 0
elif tempoServico >= 1 and tempoServico <= 3:
    bonus = 100
elif tempoServico >= 4 and tempoServico <= 6:
    bonus = 200
elif tempoServico >= 7 and tempoServico <= 10:
    bonus = 300
else:
    bonus = 500

salarioFinal = salarioAtual + reajuste + bonus

if reajuste == 0 and bonus == 0:
    print("O funcionário não tem direito a nenhum aumento.")
else:
    print(f"Salário reajustado final: R${salarioFinal:.2f}")