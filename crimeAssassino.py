print(f"responda sim ou não")

var1 = input ("Telefonou para a vítima? ")
var2 = input ("Esteve no local do crime? ")
var3 = input ("Mora perto da vítima? ")
var4 = input ("Devia para a vítima? ")
var5 = input ("Devia para a vítima? ")

pontos = 0

if var1 == "sim":
    pontos = pontos +1
if var2 == "sim":
    pontos = pontos +1
if var3 == "sim":
    pontos = pontos +1
if var4 == "sim":
    pontos = pontos +1
if var5 == "sim":
    pontos = pontos +1
    
if pontos == 2:
    print(f"com base nas analises você foi indicado como suspeito")
elif pontos == 3 or pontos == 4:
    print(f"com base nas analises você foi indicado como cumplice")
elif pontos == 5:
    print(f"não adianta fugir, ja identificamos você como o assasino, temos sua localização, a policia ja esta nas redondesas")
else:
    print(f"você foi identificado como inocente")

    #OTAVIO