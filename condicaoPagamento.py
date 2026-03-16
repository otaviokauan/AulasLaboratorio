# 1. Pedir os dados para o usuário
preco_etiqueta = float(input("Qual o preço do produto? R$ "))

print("FORMAS DE PAGAMENTO")
print("1 - Dinheiro/Cheque (10% de desconto)")
print("2 - Cartão de Crédito à vista (15% de desconto)")
print("3 - Parcelado em 2x (Preço normal)")
print("4 - Parcelado em 2x (10% de juros)")

opcao = int(input("Escolha uma opção (1-4): "))

# 2. Calcular o valor final baseado na escolha
if opcao == 1:
    desconto = preco_etiqueta * (10 / 100)
    valor_final = preco_etiqueta - desconto
    print("Você ganhou um desconto de 10%!")

elif opcao == 2:
    desconto = preco_etiqueta * (15 / 100)
    valor_final = preco_etiqueta - desconto
    print("Você ganhou um desconto de 15%!")

elif opcao == 3:
    valor_final = preco_etiqueta
    parcela = valor_final / 2
    print(f"O valor será dividido em 2x de R$ {parcela}")

elif opcao == 4:
    juros = preco_etiqueta * (10 / 100)
    valor_final = preco_etiqueta + juros
    parcela = valor_final / 2
    print(f"Com juros, as parcelas serão de R$ {parcela}")


if valor_final > 0:
    print(f"O total a pagar é: R$ {valor_final}")