litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

preco_gasolina = 2.99
preco_alcool = 2.19

valor_total = 0

if tipo == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    
    preco_com_desconto = preco_alcool * (1 - desconto)
    valor_total = litros * preco_com_desconto

elif tipo == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

    preco_com_desconto = preco_gasolina * (1 - desconto)
    valor_total = litros * preco_com_desconto

if valor_total > 0:
    print(f"O valor total a pagar é: R$ {valor_total:.2f}")