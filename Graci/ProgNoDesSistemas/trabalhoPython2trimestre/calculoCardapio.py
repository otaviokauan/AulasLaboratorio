cod = input("Digite o código do prato: ")
quantidade = int(input("Digite a quantidade: "))

if cod == "100":
    preco = 1.20
elif cod == "101":
    preco = 1.30
elif cod == "102":
    preco = 1.50
elif cod == "103":
    preco = 1.20
elif cod == "104":
    preco = 1.70
elif cod == "105":
    preco = 2.20
elif cod == "106":
    preco = 1.00
else:
    print("Código inválido")

total = preco * quantidade
print(f"Total a pagar: R$ {total:.2f}")

#Otavio