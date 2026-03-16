print("bem vindo, esse programa foi produzido por henriqucassol09")

var1 = input("qual o nome do primeiro produto")
var2 = input("qual o nome do segundo produto")
var3 = input("qual o nome do terceiro produto")
var4 = input("qual o nome do quarto produto")
var5 = input("qual o nome do quinto produto")
p1 = float (input("qual o preço do primeiro"))
p2 = float (input("qual o preço do segundo"))
p3 = float (input("qual o preço do terceiro"))
p4 = float (input("qual o preço do quarto"))
p5 = float (input("qual o preço do quinto"))

resultado = p1+p2+p3+p4+p5

print(f" os produtos comprados são {var1:g} {var2:g} {var3:g} {var4:g} {var5:g}")
print(f" os preços são respectivamente {p1:g} {p2:g} {p3:g} {p4:g} {p5:g}")
print(f"o valor total a ser pago é {resultado:g}")