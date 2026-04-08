preco = float(input("Digite o preço do produto: "))

if preco <= 50:
    valorProduto = preco * 1.05
    print(f"O preço final do produto é: {valorProduto:g}")
elif preco >= 50 and preco < 100:
    valorProduto = preco * 1.10
    print(f"O preço final do produto é: {valorProduto:g}")
elif preco >= 100:
    valorProduto = preco * 1.15
    print(f"O preço final do produto é: {valorProduto:g}")

if valorProduto <= 80:
    print("O produto é barato.")
elif valorProduto > 80 and valorProduto <= 120:
    print("O produto é normal.")
elif valorProduto > 120 and valorProduto <= 200:
        print("O produto é caro.")
else:
    print("O produto é muito caro.")

    #OTAVIO