morango = float(input("Digite o peso do morango (em KG): "))
maca = float(input("Digite o peso da maçã (em KG): "))

if morango <= 5:
    precoMorango = 2.50
else:
    precoMorango = 2.20
if maca <= 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

peso = morango + maca
preco = (precoMorango * morango) + (precoMaca * maca)

if peso > 8 or preco > 25:
    desconto = preco * 0.90

print(f"O preço total é R${preco:g}")

#OTAVIO
