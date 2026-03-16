idade = int(input("Digite a idade do nadador: "))

if idade >= 18:
    print("Categoria: Adulto")
elif idade >= 14:
    print("Categoria: JuvenilB")
elif idade >= 11:
    print("Categoria: JuvenilA")
elif idade >= 8:
    print("Categoria: InfantilB")
elif idade >= 5:
    print("Categoria: InfantilA")
else:
    print("Idade fora da categoria")